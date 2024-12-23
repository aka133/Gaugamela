from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def initialize_rag():
    
    # First, check if we already have embeddings stored
    embeddings = OpenAIEmbeddings()
    
    # Try to load existing vectorstore
    if os.path.exists("./Data/vectorstore"):
        print("Loading existing embeddings from vectorstore...")
        vectorstore = Chroma(
            persist_directory="./Data/vectorstore",
            embedding_function=embeddings
        )
    else:
        print("Creating new embeddings - this may take a while...")
        # Load and process the PDF
        loader = PyPDFLoader("./Data/decisive_battles.pdf")
        documents = loader.load()
        print(f"Loaded {len(documents)} pages from the PDF")

        # Split the documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            add_start_index=True,
        )
        texts = text_splitter.split_documents(documents)
        print(f"Split {len(texts)} texts from the PDF")

        # Create and store new embeddings
        vectorstore = Chroma.from_documents(
            texts, 
            embeddings,
            persist_directory="./Data/vectorstore"
        )
        print("Created and stored new embeddings")

    template = """You are an experienced military historian and mentor specializing in decisive battles throughout history. Your role is to:
1. First provide a clear, chronological summary of the requested battle
2. Then analyze the key strategic decisions and their impacts
3. Finally, engage in strategic discussion about specific aspects of the battle

When answering questions, maintain focus on the specific battle being discussed unless explicitly asked to make comparisons.

Use the following pieces of context to answer the question:
{context}

Question: {question}

Provide your response in this order:
1. Battle Overview (if requested)
2. Strategic Analysis
3. Discussion Points or Questions

Separate these sections with two new lines, but do not use any other demarcations. 
Do NOT say "1: Battle Overview" or "2: Strategic Analysis" or "3: Discussion Points or Questions" 
or other similar demarcations, such as "Battle Overview:" or "Strategic Analysis:" or "Discussion Points or Questions:" or anything similar.
"""
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(temperature=0.7, max_tokens=2000),  # Slightly higher temperature for more creative responses
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 6}),
        chain_type_kwargs={
            "prompt": PromptTemplate(
                template=template,
                input_variables=["context", "question"]
            ),
            "verbose": True
        }
    )
    
    return qa_chain

app = Flask(__name__)
qa_chain = initialize_rag()

@app.route('/')
def home():
    """Render the main page of our application"""
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query_documents():
    """Handle incoming questions about the textbook"""

    question = request.json.get('question') # type: ignore

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        # Use the QA chain to answer the question
        response = qa_chain.run(question)

        return jsonify({
            "question": question,
            "answer": response
        })
    
    except Exception as e:
        return jsonify({"error", str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
FROM python:3.12-slim

WORKDIR /app

# Copy only necessary requirements first
COPY requirements.txt .

# Install only the required packages
RUN pip install --no-cache-dir \
    flask \
    langchain \
    langchain-community \
    langchain-text-splitters \
    langchain-openai \
    python-dotenv \
    chromadb \
    pypdf

# Copy only the necessary files and directories
COPY src/RAG.py .
COPY templates/ ./templates
COPY Data/decisive_battles.pdf ./Data/
COPY Data/vectorstore/ ./Data/vectorstore/

# Expose the port
EXPOSE 5002

# Set environment variables
ENV FLASK_APP=RAG.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["python", "RAG.py"]
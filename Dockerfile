FROM python:3.12-slim

WORKDIR /app

# Copy only necessary requirements first
COPY requirements.txt .

# Install only the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary files and directories
COPY src/ ./src/
COPY templates/ ./templates
COPY Data/decisive_battles.pdf ./Data/
COPY Data/vectorstore/ ./Data/vectorstore/

# Set Python path to include src directory
ENV PYTHONPATH="/app/src:${PYTHONPATH}"

# Expose the port
EXPOSE 5002

# Set environment variables
ENV FLASK_APP=src/RAG.py
ENV FLASK_RUN_HOST=0.0.0.0

# Change working directory to where RAG.py is
WORKDIR /app/src

CMD ["python", "RAG.py"]
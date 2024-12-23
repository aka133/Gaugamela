FROM python:3.10-slim

# Set up base directory
WORKDIR /app

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list | grep langchain

# Copy project files
COPY src/ ./src/
COPY templates/ ./src/templates/ 
COPY Data/ ./Data/

# Set Python path to include both /app and /app/src
ENV PYTHONPATH="/app:/app/src:${PYTHONPATH}"

EXPOSE 5002

# Stay in /app directory
ENV FLASK_APP=src/RAG.py
ENV FLASK_RUN_HOST=0.0.0.0

# Keep working directory as /app
WORKDIR /app

# Debug: Print current working directory and Python path
RUN pwd && echo $PYTHONPATH

# Run using full path
CMD ["python", "src/RAG.py"]
# Base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Hugging Face default port
EXPOSE 7860

# Final CMD: run FastAPI app from server/app.py
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "7860"]

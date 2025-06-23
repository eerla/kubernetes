# Use official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY ../src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY ../src/app.py ./

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask app
CMD ["python", "app.py"] 
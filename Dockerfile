# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI application code into the container
COPY ./app.py .

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Expose the port that the FastAPI app will run on
EXPOSE 80

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

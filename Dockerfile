# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the FastAPI application code into the container
COPY app.py worldmingle-discord-sa.json ./

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn google-cloud-pubsub
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/worldmingle-discord-sa.json"

# Expose the port that the FastAPI app will run on
EXPOSE 80

# Command to run the FastAPI app with Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["bash"]

from fastapi import FastAPI
from google.cloud import pubsub_v1
import json

app = FastAPI()

# Replace 'your-project-id' and 'your-topic-name' with your actual Google Cloud project ID and Pub/Sub topic name
project_id = 'cloudcomputing-worldmingle'
topic_name = 'userLogin'

# Create a Pub/Sub publisher client
publisher = pubsub_v1.PublisherClient()

# Get the fully qualified topic path
topic_path = publisher.topic_path(project_id, topic_name)

@app.get("/")
def read_root():
    print("I am being called!")
    publish_message("Greetings from Cloud commanders! So pub/sub works")
    return {"message": "Greetings from Cloud commanders!"}

def publish_message(message: str):
    # Convert the message to bytes
    data = message.encode("utf-8")

    # Publish the message to the Pub/Sub topic
    future = publisher.publish(topic_path, data=data)
    
    # Wait for the message to be published
    future.result()
    d = {"message": f"Published message: {message}"}

    return json.dumps(d)

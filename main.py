import os
import json
from google.cloud import pubsub_v1
from discord_webhook import DiscordWebhook

# Set up Discord webhook URL
discord_webhook_url = "https://discord.com/api/webhooks/1178397830642139277/QNZjIDcqWIjHnskPIfApvxptJeicDOTHRONnG4wgs9bgXQJ8k245uQFS92IPrrswXGLq"

# Create a Pub/Sub subscriber client
subscriber = pubsub_v1.SubscriberClient()

# Replace 'your-project-id' and 'your-subscription-name' with your actual Google Cloud project ID and Pub/Sub subscription name
project_id = 'cloudcomputing-worldmingle'
subscription_name = 'userLogin-sub'

# Get the fully qualified subscription path
subscription_path = subscriber.subscription_path(project_id, subscription_name)

def send_discord_alert(message):
    # Create a Discord webhook
    webhook = DiscordWebhook(url=discord_webhook_url, content=message)
    
    # Execute the webhook
    webhook.execute()

def pubsub_callback(message):
    try:
        # Extract the message data
        message_text = message.data.decode("utf-8")
        # try:
        #     data = json.loads(data_str)
        #     message_text = data.get("message", "No message found in data.")
        # except json.JSONDecodeError:
        #     # Handle the case where the message data is not valid JSON
        #     message_text = f"Invalid JSON data: {data_str}"

        # Send a Discord alert
        send_discord_alert(f"New Pub/Sub message: {message_text}")

        # Acknowledge the message to mark it as processed
        message.ack()
    except Exception as e:
        print(f"Error processing Pub/Sub message: {e}")

def pubsub_listener(event, context):
    # Subscribe to the Pub/Sub topic
    future = subscriber.subscribe(subscription_path, callback=pubsub_callback)
    print(f"Listening for messages on {subscription_path}.")
    
    try:
        # Wait for the listener to finish (never return)
        future.result()
    except KeyboardInterrupt:
        # Unsubscribe if the function is interrupted
        future.cancel()
        print("Listener terminated.")

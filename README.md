# worldmingle

Run this command in the server (Google Compute Engine or Amazon EC2 instance)
docker run -p 80:80 abhi1604/wordmingle-culturehub:latest

Access the web app deployed from the above command via:

http://server_url:80 (http://54.163.21.24:80/) -> example run

Landing on the above URL will send messages to the Google Pub/Sub topic which is then handled by a Google Cloud Function(Lambda) which in turn sends the messages to a Discord server.

This repository also contains the Goolge Cloud function which is triggered when there are incoming messages on the Google Pub/Sub topic and sends this message to the Discord server when it successfully receives messages.



Discord server: https://discord.com/invite/NFS9UsDQ
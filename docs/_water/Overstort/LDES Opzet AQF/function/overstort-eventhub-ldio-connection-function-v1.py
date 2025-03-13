import logging
import requests
import json
from azure.functions import EventHubEvent

# Define the LDIO Workbench API endpoint
LDIO_WORKBENCH_API_URL = "http://ldio-workbench/api/data"  # Update to your LDIO endpoint

def main(event: EventHubEvent):
    for event_data in event:
        message_body = event_data.get_body().decode('utf-8')

        logging.info(f'Received message from EventHub: {message_body}')
        
        # Send the message to the LDIO Workbench
        try:
            response = requests.post(
                LDIO_WORKBENCH_API_URL,
                data=json.dumps(message_body),
                headers={'Content-Type': 'application/json'}
            )
            
            # Check if the request was successful
            response.raise_for_status()
            logging.info(f'Message pushed to LDIO Workbench: {message_body}')
        
        except requests.exceptions.RequestException as e:
            logging.error(f"Error pushing message to LDIO Workbench: {e}")

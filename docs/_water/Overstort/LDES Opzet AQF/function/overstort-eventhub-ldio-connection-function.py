import logging
import asyncio
import aiohttp
import json
from azure.functions import EventHubEvent, HttpRequest, HttpResponse
from typing import List

LDIO_PIPELINE_URLS = {
    "overstort-meting-raw": "https://ldio-overstort.test.az.aquafin.be/overstort-meting-raw",
    "overstort-meting-cleansed": "https://ldio-overstort.test.az.aquafin.be/overstort-meting-cleansed",
    "overstort-event-cleansed": "https://ldio-overstort.test.az.aquafin.be/overstort-event-cleansed",
    "overstort-event-validated": "https://ldio-overstort.test.az.aquafin.be/overstort-event-validated",
    "sensor": "https://ldio-overstort.test.az.aquafin.be/overstort-sensor"
}

async def push_to_ldio(session, message_body, pipeline_url):
    try:
        async with session.post(
            pipeline_url,
            json=message_body,
            headers={'Content-Type': 'application/json'}
        ) as response:
            response.raise_for_status()
            logging.info(f'Message pushed to LDIO Pipeline: {message_body.get("id", message_body.get("type"))}')
    except aiohttp.ClientError as e:
        logging.error(f"Error pushing message to LDIO Pipeline: {e}")

async def process_events(event_data_list, eventhub_name):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for event_data in event_data_list:
            message_body = event_data.get_body().decode('utf-8')
            json_message = json.loads(message_body)
            pipeline_url = LDIO_PIPELINE_URLS.get(eventhub_name)

            if not pipeline_url:
                logging.error(f"No pipeline configured for EventHub: {eventhub_name}")
                continue

            tasks.append(push_to_ldio(session, json_message, pipeline_url))
        await asyncio.gather(*tasks)

def main(events: List[EventHubEvent], eventhub_name: str):
    logging.info(f'Received {len(events)} messages from EventHub: {eventhub_name}')
    
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(process_events(events, eventhub_name))
    except Exception as e:
        logging.error(f"Error processing EventHub messages from {eventhub_name}: {e}")

def eventhubtest(req: HttpRequest) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

import logging
import azure.functions as func
import aiohttp
import json
import asyncio

async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HTTP trigger function processed a request.')
    
    # Add any other logic you want here
    
    return func.HttpResponse(
        "Hello, world!",
        status_code=200
    )

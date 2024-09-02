import asyncio
import os

from pyzeebe import ZeebeWorker,create_camunda_cloud_channel

import requests
import base64

channel = create_camunda_cloud_channel(
        client_id=os.environ.get('ZEEBE_CLIENT_ID'),
        client_secret=os.environ.get('ZEEBE_CLIENT_SECRET'),
        cluster_id=os.environ.get('CAMUNDA_CLUSTER_ID'),
        region=os.environ.get('CAMUNDA_CLUSTER_REGION')
    )
worker = ZeebeWorker(channel)

@worker.task(task_type="fetchAndStorePic")
async def fetch_and_store_picture(animalType : str):
    print('Fetching and Storing Picture')
    if animalType == 'cat':
        jpeg_url = "https://placecats.com/300/200"
    elif animalType == 'dog':
        jpeg_url = "https://place.dog/300/200"
    elif animalType == 'bear':
        jpeg_url = "https://placebear.com/300/200"
    else:
        raise ValueError('invalid animalType provided')
    
    response = requests.get(jpeg_url)
    # Check if the request was successful
    if response.status_code == 200:
        print('got pic successfully')
        result = {'imageData' : base64.b64encode(response.content).decode('ascii'),
                  'imageFormat' : 'jpeg'
                }
        print('Result created')
        return result;
    print('Failed to get picture')
    return "Fetch and Store Picture Failed"

loop = asyncio.get_event_loop()

if __name__ == '__main__':
    loop.run_until_complete(worker.work())
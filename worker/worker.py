import asyncio
import os
import base64

from pyzeebe import ZeebeWorker,create_camunda_cloud_channel

import requests

import psycopg2
from psycopg2 import sql

async def main():
    # Connect to the Postgres database
    try:
        conn = psycopg2.connect(
            host='postgres',
            database='images',
            user='myuser',
            password='mypassword'
        )
        print("Connected to database successfully")
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        exit(1)

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
            image_data = base64.b64encode(response.content)
            result = {'imageData' : image_data.decode('ascii'),
                    'imageFormat' : 'jpeg'
                    }
            print('Inserting result into database')
            try:
                cur = conn.cursor()
                query = sql.SQL("INSERT INTO {} (image) VALUES (%s)").format(
                    sql.Identifier('images')
                )
                cur.execute(query, (psycopg2.Binary(image_data),))
                conn.commit()
                print("Image inserted successfully")
            except psycopg2.Error as e:
                print(f"Error inserting image: {e}")            
            return result
        print('Failed to get picture')
        return "Fetch and Store Picture Failed"

    while True:
        await worker.work()

asyncio.run(main())
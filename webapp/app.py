from flask import Flask, jsonify, request, render_template
from pyzeebe import ZeebeClient, create_camunda_cloud_channel
import asyncio
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_image_url', methods=['GET'])
async def get_image_url():
    selection = request.args.get('selection')

    channel = create_camunda_cloud_channel(
        client_id=os.environ.get('ZEEBE_CLIENT_ID'),
        client_secret=os.environ.get('ZEEBE_CLIENT_SECRET'),
        cluster_id=os.environ.get('CAMUNDA_CLUSTER_ID'),
        region=os.environ.get('CAMUNDA_CLUSTER_REGION')
    )
    client = ZeebeClient(channel)
    process_instance_key, result = await client.run_process_with_result("Process_03kr6bi",
                                                                        variables = { 'animalType' : selection},
                                                                        timeout=5000)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
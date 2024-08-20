from flask import Flask, jsonify, request, render_template
from pyzeebe import ZeebeClient, create_insecure_channel
import asyncio

app = Flask(__name__)

# Mock database of images
images_db = {
    'option1': 'http://example.com/image1.jpg',
    'option2': 'http://example.com/image2.jpg',
    'option3': 'http://example.com/image3.jpg'
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_image_url', methods=['GET'])
async def get_image_url():
    selection = request.args.get('selection')
    
    channel = create_insecure_channel(hostname='localhost',port='26500')  # Will use ZEEBE_ADDRESS environment variable or localhost:26500
    client = ZeebeClient(channel)

    process_instance_key, result = await client.run_process_with_result("Process_03kr6bi")

    return jsonify({'imageUrl': images_db.get(selection, '')})

    # return result

if __name__ == '__main__':
    app.run(debug=True)
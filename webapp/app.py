from flask import Flask, jsonify, request, render_template
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
def get_image_url():
    selection = request.args.get('selection')
    return jsonify({'imageUrl': images_db.get(selection, '')})

if __name__ == '__main__':
    app.run(debug=True)
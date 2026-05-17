from flask import Flask, request, jsonify, send_from_directory
from models import analyze_image
import os

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def home():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('frontend', filename)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['image']
    image_path = "temp_image.jpg"
    file.save(image_path)
    
    result = analyze_image(image_path)
    
    os.remove(image_path)
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
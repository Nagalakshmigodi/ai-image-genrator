
from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='static')

API_KEY = 'your_actual_api_key_here'

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    url = "https://api.stability.ai/v2beta/stable-image/generate/core"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": prompt,
        "output_format": "url",
        "model": "stable-diffusion-xl-v1",
        "steps": 30,
        "width": 768,
        "height": 768
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        image_url = response.json()['image']
        return jsonify({'image_url': image_url})
    else:
        return jsonify({'error': 'Image generation failed', 'details': response.json()}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)

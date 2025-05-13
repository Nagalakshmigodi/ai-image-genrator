from flask import Flask, request, jsonify, send_from_directory
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

import os

app = Flask(__name__, static_folder='static')

# Your API key from Stability AI
os.environ['STABILITY_KEY'] = 'sk-tZv2XIDQywGvScTR7QT7owr74AxEjgQlKzrmJ4tyehcwxdSz'

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
)

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({'error': 'Prompt required'}), 400

    try:
        answers = stability_api.generate(
            prompt=prompt,
            steps=30,
            width=512,
            height=512,
            cfg_scale=8.0,
            sampler=generation.SAMPLER_K_DPM_2_ANCESTRAL,
        )

        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    return jsonify({'error': 'Safety filter triggered. Try another prompt.'})
                if artifact.type == generation.ARTIFACT_IMAGE:
                    # Save image locally
                    img_path = f"static/generated.png"
                    with open(img_path, "wb") as f:
                        f.write(artifact.binary)
                    return jsonify({'image_url': '/static/generated.png'})

        return jsonify({'error': 'No image generated'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

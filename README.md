# 🎨 AI Image Generator

A simple web app to generate AI images based on text prompts using the Stability AI API (Stable Diffusion). Built with Flask and a clean, pastel-themed HTML/CSS frontend.

---

## 🚀 Features

- Generate AI images from custom prompts
- Clean, responsive UI
- Built using Flask (Python) for the backend
- Uses Stability AI (Stable Diffusion) via API
- Soft pastel design with modern UI

---

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Backend    | Python, Flask            |
| Frontend   | HTML, CSS, Vanilla JS    |
| API        | Stability AI (Stable Diffusion API) |

---

## 📁 File Structure

image-generator-app/
│
├── app.py # Flask backend logic
├── requirements.txt # Python dependencies
│
├── static/
│ ├── index.html # Web frontend
│ └── style.css # Custom CSS styling


---

## ⚙️ How It Works

1. User enters a text prompt in the browser.
2. The frontend sends a POST request to the `/generate` Flask route.
3. The Flask server sends the prompt to Stability AI's API.
4. Stability AI returns an image URL.
5. The frontend displays the generated image.

---

## 🔐 API Used – Stability AI

- Endpoint: `https://api.stability.ai/v2beta/stable-image/generate/core`
- Requires an API key. Get yours from [platform.stability.ai](https://platform.stability.ai)

---

## ▶️ How to Run Locally

1. Clone the repo or create a new folder:

```bash
git clone https://github.com/your-username/image-generator-app.git
cd image-generator-app
Create and activate a virtual environment (optional but recommended):

2.Create and activate a virtual environment (optional but recommended):
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
3.Install dependencies:
pip install -r requirements.txt
4.Run the app:
python app.py


Sample Prompts
. a man holding a watermelon

. a fantasy castle on a floating island

. a futuristic robot reading a book

. a cozy cabin in a snowy forest




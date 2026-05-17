# Image Captioning AI - Multimodal AI System

An end-to-end multimodal AI system that automatically generates captions and summaries for uploaded images using deep learning.

## Demo
Upload any image → AI generates a caption → Summarizes it instantly

## Tech Stack
- **Python** - Backend logic
- **Flask** - REST API
- **HuggingFace Transformers** - AI models
- **VisionEncoderDecoder (ViT + GPT2)** - Image captioning
- **DistilBART** - Text summarization
- **HTML/CSS/JavaScript** - Frontend UI

##  How It Works
1. User uploads an image via the frontend
2. Flask API receives the image
3. ViT encodes the image into features
4. GPT2 generates a caption from the features
5. DistilBART summarizes the caption
6. Result is returned to the frontend

## Installation

```bash
git clone https://github.com/AratiSutar/image-captioning-ai.git
cd image-captioning-ai
python -m venv venv
venv\Scripts\activate
pip install flask transformers torch Pillow
python app.py
```

## Project Structure
```
image-captioning-ai/
├── app.py          # Flask backend
├── models.py       # AI models
├── frontend/
│   ├── index.html  # UI
│   ├── style.css   # Styling
│   └── scripts.js  # Frontend logic
```

## Results
- Accurately captions animals, people, objects and scenes
- Works on CPU — no GPU required

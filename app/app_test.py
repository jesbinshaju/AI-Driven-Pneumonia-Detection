from flask import Flask, render_template, request, jsonify
from fastai.vision.all import *
import pathlib

# Fix for Windows path compatibility
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

app = Flask(__name__)

# --- TEMPORARY BYPASS ---
try:
    learn = load_learner('../models/model_export.pkl')
    model_loaded = True
except Exception as e:
    print(f"Model not found, running in demo mode: {e}")
    model_loaded = False
# ------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if not model_loaded:
        return jsonify({'result': 'Model Not Loaded', 'confidence': '0.00'})
    
    img_file = request.files['file']
    img = PILImage.create(img_file)
    pred, pred_idx, probs = learn.predict(img)
    return jsonify({'result': str(pred), 'confidence': f'{probs[pred_idx]:.2f}'})

if __name__ == '__main__':
    app.run(debug=True)
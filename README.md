# AI-Driven Pneumonia Detection: Diagnostic Pipeline

This repository hosts a clinical-grade diagnostic engine optimized for the automated classification of pneumonia via thoracic radiography. The architecture focuses on **Transfer Learning**, leveraging deep convolutional neural networks to achieve high-sensitivity feature extraction.

---

## ⚙️ Technical Architecture

### 1. Model & Training Pipeline
*   **Backbone:** Utilizes a ResNet (Residual Network) architecture, employing skip-connections to mitigate the vanishing gradient problem in deep training.
*   **Transfer Learning:** Implements fine-tuning on pre-trained weights to adapt spatial feature extractors from generic large-scale datasets (ImageNet) to the specific distribution of medical X-ray imagery.
*   **Data Augmentation:** Features an automated augmentation pipeline (affine transformations, normalization, and resizing) to improve model generalizability and reduce overfitting.
*   **Optimization:** Configured for CUDA-enabled throughput, utilizing SGD with momentum and 1-cycle policy learning rate scheduling.

### 2. Inference Engine
*   **FastAI / PyTorch Framework:** Uses the `fastai.vision.learner` API for production-ready inference, abstracting complex tensor operations into a high-performance predictive pipeline.
*   **Deployment:** Decoupled architecture serving via Flask (WSGI). Inference is executed in a controlled environment with CPU/GPU dynamic mapping, ensuring low-latency results.

### 3. Data & Preprocessing
*   **Preprocessing:** Standardized input normalization to ensure distribution consistency across the training/validation sets.
*   **Inference Logic:** Dynamic conversion of input buffers to `PILImage` objects, maintaining spatial integrity through fixed-dimension resizing.

---

## 🛠 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Deep Learning** | PyTorch, FastAI |
| **Backend** | Flask (WSGI) |
| **Environment** | Python 3.13 (Venv) |
| **Hardware Acceleration** | NVIDIA CUDA 11.8+ (RTX 2050) |
| **Interface** | HTML5/CSS (Asynchronous Fetch API) |

---

## 📁 Project Structure

```text
Pneumonia-Detection-Project/
├── app/               # Flask server and UI templates
│   ├── static/        # CSS and frontend assets
│   └── templates/     # HTML interface
├── data/              # Training/Validation datasets
├── models/            # Exported .pkl model (The "Brain")
├── notebook/          # Training and experimentation zone
├── .gitignore         # File exclusion rules
├── requirements.txt   # Dependencies
└── README.md          # Project documentation



Project Structre

Pneumonia-Detection-Project/
├── data/                   # Keep your training data here
│   ├── train/
│   └── test/
├── notebook/               # Training zone
│   └── train_model.ipynb   # The FastAI code to create the .pkl
├── app/                    # Deployment zone
│   ├── app.py              # Flask server
│   ├── static/             # JS & CSS
│   └── templates/          # HTML
├── models/                 # Where your trained 'brain' lives
│   └── model_export.pkl
├── requirements.txt        # Shared dependencies
└── README.md

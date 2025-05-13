# Arogyam - AI Health Assistant

*Arogyam* is an AI-based health prediction tool currently supporting:

- *Heart Disease Prediction*
- *Diabetes Prediction*

Both modules use machine learning models trained on UCI datasets and include Streamlit-based interactive apps.

## Features

- Smart predictions using trained models  
- Clean UI with prediction confidence  
- Modular and scalable project structure  
- Basic authentication system (Login/Signup/Logout)
- Integrated chatbot powered by DistilBERT and DuckDuckGo for smart health answers

## Future Scope

- Add more disease modules: Parkinson’s, Lung Cancer, Skin Disease Detection (CV), Pneumonia Detection (CV), Brain Tumor Detection (CV), etc.  
- Include nutrition, fitness, and mental health support  
- Deploy with login, chatbot, and emergency features  

## How to Run

```bash
pip install -r requirements.txt
python -m streamlit run src/app.py

## Folder Structure

diseases_prediction_project/
│
├── .venv/                         # Virtual environment
├── data/
│   ├── raw/                       # Raw datasets
│   └── processed/                 # Cleaned datasets
│
├── models/
│   ├── diabetes_model.pkl
│   ├── heart_model.pkl
│   └── heart_scaler.pkl
│
├── notebook/
│   ├── eda.ipynb
│   ├── heart_data_cleaning.ipynb
│   ├── model_training.ipynb
│   └── model_visualization.ipynb
│
├── src/
│   ├── app.py                     # Main app file
│   ├── auth.py                    # Login/Signup logic
│   ├── predict.py
│   ├── preprocessing.py
│   ├── save_model.py
│   ├── nlp_engine.py              # Chatbot logic (DistilBERT + DuckDuckGo)
│   └── streamlit_apps/
│       ├── app_diabetes.py
│       ├── app_heart.py
│       ├── app_login.py
│       ├── app_chatbot.py
│       └── _init_.py
│
├── requirements.txt
├── README.md
└── .gitignore

## License
This project is licensed under the MIT License.
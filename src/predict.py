import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the saved model
with open('D:/ai internship/disease_prediction_project/models/diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# New input data (Example)
new_data = {
    'Pregnancies': [6],
    'Glucose': [148],
    'BloodPressure': [72],
    'SkinThickness': [35],
    'Insulin': [0],
    'BMI': [33.6],
    'DiabetesPedigreeFunction': [0.627],
    'Age': [50]
}

# Convert new data to DataFrame
new_data_df = pd.DataFrame(new_data)

# Feature Scaling (same as training)
scaler = StandardScaler()
new_data_scaled = scaler.fit_transform(new_data_df)

# Make a prediction
prediction = model.predict(new_data_scaled)

# Display the prediction
if prediction[0] == 1:
    print("Prediction: Diabetes (1)")
else:
    print("Prediction: No Diabetes (0)")

import joblib
import numpy as np

def predict_heart_disease(data):
    try:
        model = joblib.load("models/heart_model.pkl")
        scaler = joblib.load("models/heart_scaler.pkl")
        data_scaled = scaler.transform([data])
        prediction = model.predict(data_scaled)[0]
        return prediction
    except Exception as e:
        print("Error in heart prediction:", e)
        return None
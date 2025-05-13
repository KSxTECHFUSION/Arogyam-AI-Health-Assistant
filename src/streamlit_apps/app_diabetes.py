import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('D:/ai internship/disease_prediction_project/data/raw/diabetes.csv')

# Feature Matrix (X) and Target Variable (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Calculate training and testing accuracy
train_accuracy = model.score(X_train, y_train)
test_accuracy = model.score(X_test, y_test)

# Streamlit app interface
def main():
    st.title('🩺 Diabetes Prediction')
    st.markdown("### Model Performance")
    st.write(f"✅ Training Accuracy: *{train_accuracy * 100:.2f}%*")
    st.write(f"✅ Testing Accuracy: *{test_accuracy * 100:.2f}%*")

    st.markdown("---")
    st.markdown("### Please enter the following information:")

    # Input fields organized in two columns
    col1, col2 = st.columns(2)

    with col1:
        pregnancies = st.number_input('Pregnancies (Number of pregnancies the person has had)', min_value=0)
        blood_pressure = st.slider('Blood Pressure (mm Hg)', 0, 180, 70)
        insulin = st.slider('Insulin (mu U/ml)', 0, 900, 80)
        dpf = st.number_input('Diabetes Pedigree Function (A function that scores likelihood of diabetes based on family history)', min_value=0.0, max_value=2.5, value=0.5)

    with col2:
        glucose = st.slider('Glucose Level (Blood glucose level)', 0, 300, 120)
        skin_thickness = st.slider('Skin Thickness (mm)', 0, 100, 20)
        bmi = st.number_input('BMI (Body Mass Index)', min_value=0.0, max_value=70.0, value=25.0)
        age = st.slider('Age (Age of the person)', 0, 120, 30)

    # Create input dictionary
    input_dict = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    st.markdown("---")
    st.subheader("Your Input Overview")
    fig, ax = plt.subplots()
    ax.bar(input_dict.keys(), input_dict.values(), color='#FF4B4B')
    plt.xticks(rotation=45)
    plt.ylabel("Values")
    plt.title("Entered Health Parameters")
    st.pyplot(fig)

    st.markdown("---")
    
    # Prediction logic when the user clicks the 'Predict' button
    if st.button('🔮 Predict'):
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
        input_data_scaled = scaler.transform(input_data)

        # Prediction and probability
        prediction = model.predict(input_data_scaled)
        probability = model.predict_proba(input_data_scaled)[0][1]

        # Define risk level and corresponding color coding
        if probability < 0.3:
            risk = "Low Risk 🔵"
            color = "#d4edda"
            emoji = "✅"
            text_color = "green"
            probability_color = "green"
        elif probability < 0.7:
            risk = "Moderate Risk 🟡"
            color = "#fff3cd"
            emoji = "⚠"
            text_color = "orange"
            probability_color = "orange"
        else:
            risk = "High Risk 🔴"
            color = "#f8d7da"
            emoji = "❌"
            text_color = "red"
            probability_color = "red"

        st.markdown(f"""
            <div style="background-color:{color};padding:15px;border-radius:10px">
                <h4 style="color:{text_color};">Prediction: {emoji} {'Diabetes (1)' if prediction[0] == 1 else 'No Diabetes (0)'}</h4>
                <p style="color:{text_color};font-weight:bold">Risk Level: {risk}</p>
                <p style="color:{probability_color};">Probability of Diabetes: {probability * 100:.2f}%</p>
            </div>
            """, unsafe_allow_html=True)

    # Add Reset Button for User Input
    if st.button('🔄 Reset'):
        #st.session_state.clear()
        st.rerun()

# This is the function your main app.py will call
def run():
    main()
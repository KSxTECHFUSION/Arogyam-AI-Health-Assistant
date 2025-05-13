import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

def main():
    st.title('💓 Heart Disease Prediction')

    # Load dataset
    df = pd.read_csv('data/raw/heart_disease.csv')
    X = df.drop('target', axis=1)
    y = df['target']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, y_train)

    train_accuracy = model.score(X_train, y_train)
    test_accuracy = model.score(X_test, y_test)

    st.markdown("### Model Performance")
    st.success(f"✅ Training Accuracy: {train_accuracy * 100:.2f}%")
    st.success(f"✅ Testing Accuracy: {test_accuracy * 100:.2f}%")

    st.markdown("---")
    st.markdown("### Please enter the values below:")

    # Inputs organized with explanations
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input('Age (Patient\'s age in years)', min_value=0)

        sex_option = st.selectbox('Sex', ('Male', 'Female'))
        sex = 1 if sex_option == 'Male' else 0

        cp_option = st.selectbox('Chest Pain Type', ('Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'))
        cp_mapping = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
        cp = cp_mapping[cp_option]

        trestbps = st.number_input('Resting Blood Pressure (mm Hg at hospital admission)', min_value=0)

        chol = st.number_input('Serum Cholesterol (mg/dl)', min_value=0)

        fbs_option = st.selectbox('Fasting Blood Sugar', ('> 120 mg/dl', '<= 120 mg/dl'))
        fbs = 1 if fbs_option == '> 120 mg/dl' else 0

    with col2:
        restecg_option = st.selectbox('Resting ECG Results', ('Normal', 'ST-T Wave Abnormality', 'Left Ventricular Hypertrophy'))
        restecg_mapping = {'Normal': 0, 'ST-T Wave Abnormality': 1, 'Left Ventricular Hypertrophy': 2}
        restecg = restecg_mapping[restecg_option]

        thalach = st.number_input('Max Heart Rate Achieved (during exercise test)', min_value=0)

        exang_option = st.selectbox('Exercise Induced Angina', ('Yes', 'No'))
        exang = 1 if exang_option == 'Yes' else 0

        oldpeak = st.number_input('Oldpeak (ST depression induced by exercise relative to rest)', min_value=0.0)

        slope_option = st.selectbox('Slope of ST Segment', ('Upsloping', 'Flat', 'Downsloping'))
        slope_mapping = {'Upsloping': 0, 'Flat': 1, 'Downsloping': 2}
        slope = slope_mapping[slope_option]

        ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', [0, 1, 2, 3])

        thal_option = st.selectbox('Thalassemia', ('Normal (3)', 'Fixed Defect (6)', 'Reversible Defect (7)'))
        thal_mapping = {'Normal (3)': 3, 'Fixed Defect (6)': 6, 'Reversible Defect (7)': 7}
        thal = thal_mapping[thal_option]

    # Bar chart of inputs
    input_dict = {
        "Age": age, "Sex": sex, "Chest Pain": cp, "Resting BP": trestbps, "Cholesterol": chol,
        "FBS": fbs, "ECG": restecg, "Max HR": thalach, "Angina": exang,
        "Oldpeak": oldpeak, "ST Slope": slope, "Vessels": ca, "Thal": thal
    }

    st.subheader("Your Input Overview")
    fig, ax = plt.subplots()
    ax.bar(input_dict.keys(), input_dict.values(), color='skyblue')
    plt.xticks(rotation=45)
    plt.ylabel("Value")
    plt.title("Entered Health Parameters")
    st.pyplot(fig)

    # Prediction button
    if st.button('🔮 Predict'):
        try:
            input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                                    thalach, exang, oldpeak, slope, ca, thal]])
            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)
            probability = model.predict_proba(input_scaled)[0][1]

            # Define risk level and colors
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
                    <h4 style="color:{text_color};">Prediction: {emoji} {'Heart Disease (1)' if prediction[0] == 1 else 'No Heart Disease (0)'}</h4>
                    <p style="color:{text_color};font-weight:bold">Risk Level: {risk}</p>
                    <p style="color:{probability_color};font-weight:bold">Probability of Heart Disease: {probability * 100:.2f}%</p>
                </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Prediction error: {str(e)}")

    if st.button('🔄 Reset'):
       # st.session_state.clear()
        st.rerun()

def run():
    main()
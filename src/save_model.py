import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Load data
df = pd.read_csv('D:/ai internship/disease_prediction_project/data/raw/diabetes.csv')
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Preprocess
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model using Pickle
with open('D:/ai internship/disease_prediction_project/models/diabetes_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model saved successfully!")
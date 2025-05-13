import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('D:/ai internship/disease_prediction_project/data/raw/diabetes.csv')

# Feature Matrix (X) and Target Variable (y)
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# (Optional) Save the processed data
processed_df = pd.DataFrame(X_scaled, columns=X.columns)
processed_df['Outcome'] = y.values
processed_df.to_csv('D:/ai internship/disease_prediction_project/data/processed/diabetes_cleaned.csv', index=False)

print("Preprocessing complete. Processed data saved successfully!")
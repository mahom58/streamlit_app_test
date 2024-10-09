import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# load data
heart = pd.read_csv(r'C:\Users\41536\Documents\greenbootcamps\Project_HeartDisease\clean_data.csv')
heart.head()

heart = heart.drop(columns=['num'])

# Prepare features and target variable
X = heart.drop('heart_disease',axis=1)
y = heart['heart_disease']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the RandomForest model
best_rf_model = RandomForestClassifier(n_estimators = 200, min_samples_split = 5, min_samples_leaf = 4, max_depth = 20)
best_rf_model.fit(X_train, y_train)

# Streamlit app title
st.title("Heart Disease Prediction App")

# Instructions for the user
st.write("""
    Enter the feature values to predict the presence of heart disease using the Random Forest model.
""")

# Input fields for user features
age = st.slider('Age', 0, 120, 50)
sex = st.selectbox('Sex', options=[0, 1])  # 0 = female, 1 = male
cp = st.selectbox('Chest Pain Type', options=[0, 1, 2, 3])
trestbps = st.slider('Resting Blood Pressure (mm Hg)', 80, 200, 120)
chol = st.slider('Cholesterol (mg/dl)', 100, 600, 200)
fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1])
restecg = st.selectbox('Resting Electrocardiographic Results', options=[0, 1, 2])
thalach = st.slider('Maximum Heart Rate Achieved', 60, 220, 150)
exang = st.selectbox('Exercise Induced Angina', options=[0, 1])
oldpeak = st.slider('Oldpeak (depression induced by exercise relative to rest)', 0.0, 6.0, 1.0)
slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=[0, 1, 2])
ca = st.selectbox('Number of Major Vessels (0-3) Colored by Fluoroscopy', options=[0, 1, 2, 3])
thal = st.selectbox('Thalassemia', options=[0, 1, 2, 3])

# Put user input into a DataFrame
input_data = pd.DataFrame({
    'age': [age],
    'sex': [sex],
    'cp': [cp],
    'trestbps': [trestbps],
    'chol': [chol],
    'fbs': [fbs],
    'restecg': [restecg],
    'thalach': [thalach],
    'exang': [exang],
    'oldpeak': [oldpeak],
    'slope': [slope],
    'ca': [ca],
    'thal': [thal]
})

# When the user presses the 'Predict' button
if st.button('Predict'):
    # Make prediction
    prediction = best_rf_model.predict(input_data)

    # Assuming the output is binary (0 = no heart disease, 1 = heart disease)
    predicted_class = "Heart Disease" if prediction[0] == 1 else "No Heart Disease"
    
    # Display the results
    st.write(f"Predicted Class: {predicted_class}")

# Footer
st.write("This app uses a retrained RandomForestClassifier to predict the presence of heart disease.")

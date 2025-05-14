import streamlit as st
import requests

# Define the API URL
api_url = "http://127.0.0.1:5000/predict"

# Create a simple form for user input
st.title("Heart Failure Prediction")

# Provide descriptions for the user
st.subheader("Enter Patient Details Below:")

age = st.number_input("Age", min_value=0, max_value=120, value=50)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")

# Chest Pain Type
cp = st.selectbox(
    "Chest Pain Type",
    options=[0, 1, 2, 3],
    format_func=lambda x: {
        0: "No Chest Pain",
        1: "Typical Angina",
        2: "Atypical Angina",
        3: "Non-Anginal Pain"
    }.get(x)
)

trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=130)
chol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=600, value=250)

# Fasting Blood Sugar
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

# Resting Electrocardiographic Results
restecg = st.selectbox(
    "Resting Electrocardiographic Results",
    options=[0, 1, 2],
    format_func=lambda x: {
        0: "Normal",
        1: "Having ST-T wave abnormality",
        2: "Showing probable or definite left ventricular hypertrophy"
    }.get(x)
)

thalach = st.number_input("Maximum Heart Rate Achieved (bpm)", min_value=50, max_value=250, value=160)

# Exercise Induced Angina
exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

# Depression Induced by Exercise
oldpeak = st.number_input("Depression Induced by Exercise (ST segment depression)", min_value=0.0, max_value=10.0, value=1.2)

# Slope of the Peak Exercise ST Segment
slope = st.selectbox(
    "Slope of the Peak Exercise ST Segment",
    options=[0, 1, 2],
    format_func=lambda x: {
        0: "Upsloping",
        1: "Flat",
        2: "Downsloping"
    }.get(x)
)



# Collect the data into a dictionary
data = {
    "Age": age,
    "Sex": sex,
    "ChestPainType": cp,
    "RestingBP": trestbps,
    "Cholesterol": chol,
    "FastingBS": fbs,
    "RestingECG": restecg,
    "MaxHR": thalach,
    "ExerciseAngina": exang,
    "Oldpeak": oldpeak,
    "ST_Slope": slope
}


# Send data to the Flask API and get the prediction
if st.button("Predict"):
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        if prediction == 0:
            st.write("Prediction: No Heart Disease")
        else:
            st.write("Prediction: Heart Disease")
    else:
        st.write(f"Error: {response.json().get('error')}")

import streamlit as st
import requests

api_url = "http://127.0.0.1:5000/predict"

st.title("Heart Failure Prediction")
st.subheader("Enter Patient Details Below:")

# Numerical Inputs
age = st.number_input("Age", min_value=0, max_value=120, value=None, format="%d")
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=None, format="%d")
chol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=600, value=None, format="%d")
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=50, max_value=250, value=None, format="%d")
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=None, format="%.1f")

# Categorical Inputs with default placeholder "Select"
sex = st.selectbox(
    "Sex",
    options=["Select", "F", "M"],
    format_func=lambda x: {"Select": "Select", "F": "Female", "M": "Male"}[x]
)

cp = st.selectbox(
    "Chest Pain Type",
    options=["Select", "NAP", "ATA", "ASY", "TA"],
    format_func=lambda x: {
        "Select": "Select",
        "NAP": "Non-Anginal Pain",
        "ATA": "Atypical Angina",
        "ASY": "Asymptomatic",
        "TA": "Typical Angina"
    }[x]
)

fbs = st.selectbox(
    "Fasting Blood Sugar > 120 mg/dl",
    options=["Select", 0, 1],
    format_func=lambda x: "Select" if x == "Select" else ("Yes" if x else "No")
)

restecg = st.selectbox(
    "Resting ECG",
    options=["Select", "Normal", "ST", "LVH"]
)

exang = st.selectbox(
    "Exercise Induced Angina",
    options=["Select", "N", "Y"],
    format_func=lambda x: {"Select": "Select", "N": "No", "Y": "Yes"}[x]
)

slope = st.selectbox(
    "ST Slope",
    options=["Select", "Up", "Flat", "Down"]
)

# Create input dictionary
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

# Validation and Prediction
if st.button("Predict"):
    # Check for empty numeric inputs
    if None in [age, trestbps, chol, thalach, oldpeak]:
        st.warning("Please fill in all numerical fields.")
    # Check for unselected dropdowns
    elif "Select" in [sex, cp, fbs, restecg, exang, slope]:
        st.warning("Please make selections for all dropdown fields.")
    else:
        response = requests.post(api_url, json=data)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.success("Prediction: No Heart Disease" if prediction == 0 else "Prediction: Heart Disease")
        else:
            st.error(f"Error: {response.json().get('error')}")

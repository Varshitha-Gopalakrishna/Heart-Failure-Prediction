# 💓 Heart Failure Prediction App

This project predicts the likelihood of heart failure based on patient data using a machine learning model. It features a RESTful Flask API deployed on AWS EC2 and an interactive Streamlit frontend deployed on Streamlit Cloud.

---

## 📌 Project Overview

- 🧠 **Machine Learning Model**: Trained on heart disease data with preprocessing (LabelEncoding, Scaling) and optimized using XGBoost.
- ⚙️ **Backend**: Flask API to serve predictions.
- 🖼️ **Frontend**: Streamlit app to collect user input and display results.
- ☁️ **Deployment**: 
  - **Flask API** on **AWS EC2** (Free Tier)
  - **Streamlit App** on **Streamlit Cloud**
- 📁 **Organized project structure** with modular code.

---

## 🧪 Sample Prediction Input

```json
{
  "Age": 60,
  "Sex": "M",
  "ChestPainType": "ASY",
  "RestingBP": 140,
  "Cholesterol": 250,
  "FastingBS": 0,
  "RestingECG": "Normal",
  "MaxHR": 150,
  "ExerciseAngina": "N",
  "Oldpeak": 1.5,
  "ST_Slope": "Flat"
}
---

## 🗂️ Project Structure
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── model_utils.py
├── models/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── encoders.pkl
├── data/
│   └── heart.csv
├── EDA/
│   └── heart failure prediction.ipynb
├── streamlit_app.py
├── train_model.py
├── app.py
├── requirements.txt
├── .gitignore
├── test_api.py
├── test_post.py
└── README.md
---

☁️ Deployment Details

🔹 Flask API on AWS EC2 (Free Tier)
🔹 Streamlit App on Streamlit Cloud


✍️ Author
Varshitha Gopalakrishna
LinkedIn | GitHub

📄 License
This project is for educational/demo purposes.
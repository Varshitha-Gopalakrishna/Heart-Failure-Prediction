# Heart Failure Prediction

A machine learning web application that predicts whether a person is likely to have heart disease based on their health indicators such as age, chest pain type, blood pressure, cholesterol, ECG, etc.

## 📁 Project Structure

Heart-Failure-Prediction/
│
├── app/
│ └── streamlit_app.py # Streamlit UI code
│
├── data/
│ └── heart.csv # Original dataset
│
├── models/
│ ├── model.pkl # Trained ML model
│ └── label_mappings.json.gz # Label mappings if needed
│
├── src/
│ ├── data_preprocessing.py # Preprocessing functions
│ ├── train_model.py # Model training & saving
│ └── prediction_pipeline.py # Prediction function
│
├── venv/ # Virtual environment (not pushed to GitHub)
├── requirements.txt # List of required packages
├── README.md # This file
└── .gitignore # Files to ignore in Git



✍️ Author
Varshitha Gopalakrishna
LinkedIn | GitHub
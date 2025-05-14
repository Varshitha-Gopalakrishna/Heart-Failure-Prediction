import pandas as pd
import dill

def load_model_and_preprocessors():
    with open("models/model.pkl", "rb") as f:
        model = dill.load(f)
    with open("models/scaler.pkl", "rb") as f:
        scaler = dill.load(f)
    with open("models/encoders.pkl", "rb") as f:
        encoders = dill.load(f)
    return model, scaler, encoders

def preprocess_input(data, encoders, scaler):
    try:
        input_df = pd.DataFrame([data])
        for col, encoder in encoders.items():
            if col in input_df.columns:
                input_df[col] = encoder.transform(input_df[col])
        input_scaled = scaler.transform(input_df)
        return input_scaled
    except Exception as e:
        raise ValueError(f"Preprocessing error: {e}")

def predict_heart_failure(data):
    try:
        model, scaler, encoders = load_model_and_preprocessors()
        processed = preprocess_input(data, encoders, scaler)
        prediction = model.predict(processed)
        return {"prediction": int(prediction[0])}
    except Exception as e:
        return {"error": f"Prediction error: {e}"}
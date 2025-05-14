from flask import Blueprint, request, jsonify, render_template
from app.model_utils import predict_heart_failure

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        result = predict_heart_failure(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": f"Server error: {e}"})
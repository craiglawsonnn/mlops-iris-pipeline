import joblib
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

model = joblib.load("models/model.pkl")

class_names = ["setosa", "versicolor", "virginica"]


@app.route("/")
def home():
    return jsonify({
        "message": "Iris Classification API is running",
        "endpoint": "/predict"
    })


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"]
    ]])

    prediction = model.predict(features)[0]

    return jsonify({
        "prediction": class_names[prediction]
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
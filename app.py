from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Get current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Load model and vectorizer
svc_model = joblib.load(os.path.join(current_dir, "model", "svc.pkl"))
tfidf = joblib.load(os.path.join(current_dir, "model", "tfidf_vectorizer.pkl"))

# Labels
labels = {0: "Hate Speech", 1: "Offensive Language", 2: "Neither"}

# Routes
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict():
    user_text = request.form["user_text"]
    text_vector = tfidf.transform([user_text])
    prediction = svc_model.predict(text_vector)[0]
    result = labels.get(prediction, "Unknown")

    return render_template("index.html", prediction=result, input_text=user_text)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "7860"))
    app.run(host="0.0.0.0", port=port, debug=True)

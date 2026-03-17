# ⚡ Text Detection: Hate Speech & Offensive Language Classifier

This project is an end-to-end NLP solution designed to detect and categorize harmful content in text. By leveraging machine learning, it provides an automated way to monitor online discourse, ensuring safer digital environments.



### 🌐 [Live Demo on Hugging Face Spaces](https://huggingface.co/spaces/Zainch032/Text-Detection)

---

## 🚀 The Problem & Solution

**The Problem:** Manual moderation of social media, comments, and forums is impossible at scale. Distinguishing between genuine "Hate Speech," "Offensive Language," and "Neutral" text is nuanced and context-dependent.

**The Solution:** This app provides a real-time classification tool. By using a **Supportive Vector Classifier (SVC)** paired with **TF-IDF vectorization**, the system identifies linguistic patterns associated with harmful behavior, allowing platforms to flag or filter content instantly.

---

## 🛠️ Data Preprocessing & Accuracy Boost

To ensure the model focuses on the *meaning* of the text rather than digital noise, we implemented a rigorous preprocessing pipeline. This was critical for improving the F1-score and overall accuracy:

1.  **Noise Removal:** Stripping out URLs, HTML tags, and special characters that don't contribute to sentiment.
2.  **Normalization:** Converting all text to lowercase to ensure `Hate` and `hate` are treated identically.
3.  **Tokenization & Cleaning:** Removing extra whitespace and stop words that dilute the model's focus.
4.  **TF-IDF Vectorization:** We used **Term Frequency-Inverse Document Frequency** to weigh unique, meaningful words more heavily than common filler words.



---

## 🏗️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Machine Learning** | Python, Scikit-Learn, Pandas, Numpy |
| **NLP Techniques** | TF-IDF Vectorization, Text Normalization |
| **Model** | Support Vector Classifier (SVC) |
| **Web Framework** | Flask (Jinja2 Templates) |
| **Deployment** | Docker, Gunicorn, Hugging Face Spaces |

---

## 📂 Project Structure

```text
├── app.py                # Flask application entry point
├── model/                # Serialized model artifacts
│   ├── svc.pkl           # Trained SVC Model
│   └── tfidf_vectorizer.pkl
├── notebooks/            # Research & Development
│   └── model_training.ipynb
├── static/               # CSS & UI styling
├── templates/            # HTML frontend
├── Dockerfile            # Containerization instructions
└── requirements.txt      # Project dependencies
```

---

## 💻 Local Development

### Using Python
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run App:**
   ```bash
   python app.py
   ```
3. **Access:** Open `http://127.0.0.1:7860`

### Using Docker
```bash
# Build the image
docker build -t text-detection-app .

# Run the container
docker run -p 7860:7860 text-detection-app
```

---

## ⚖️ Classification Labels
The model categorizes input into three distinct buckets:
* **Hate Speech:** Discriminatory language targeting protected groups.
* **Offensive Language:** Profanity or derogatory terms without specific hate intent.
* **Neither:** Clean, neutral, or positive text.


---
title: Text Detection
emoji: ⚡
colorFrom: yellow
colorTo: gray
sdk: docker
pinned: false
---

<<<<<<< HEAD
hf

=======
>>>>>>> d6832e31e439072de081850002c54f6902723475
## Text Detection NLP App

This project is an end-to-end NLP pipeline for hate/offensive language detection. It includes **data cleaning**, **exploratory data analysis (EDA)**, **model training**, and **deployment of an NLP classifier** as a web app.

<<<<<<< HEAD
## What this “chatbot” does

You type a message into the web UI, and the app returns a **single classification label**:

- **Hate Speech**
- **Offensive Language**
- **Neither**

Under the hood it is a classic NLP classifier: **TF‑IDF vectorizer → SVC model**.

=======
>>>>>>> d6832e31e439072de081850002c54f6902723475
## Features

- **Data cleaning**: text normalization (lowercasing, punctuation/whitespace handling, basic noise removal).
- **EDA**: label distribution, text length exploration, and qualitative inspection of examples to understand the dataset.
- **Modeling**: TF-IDF vectorization with an SVC classifier (serialized with `joblib` and loaded at inference time).
- **Web UI**: simple Flask interface where users can input text and get predictions (Hate Speech, Offensive Language, Neither).
- **Deployment ready**: containerized with Docker for reproducible deployment.

<<<<<<< HEAD
## Preprocessing (training + inference)

During training (see `notebooks/model_training.ipynb`), text is cleaned before vectorization. Typical steps used in this project:

- **Lowercasing**
- **Whitespace normalization** (remove extra spaces/newlines)
- **Noise removal** (basic punctuation/special-character cleanup depending on dataset)

The trained **TF‑IDF vectorizer** (`model/tfidf_vectorizer.pkl`) must be used at inference time to transform user input in the same way training features were created.

## How deployment works

- The Flask app (`app.py`) loads:
  - `model/svc.pkl`
  - `model/tfidf_vectorizer.pkl`
- It transforms the user text using TF‑IDF and predicts a label with the SVC model.
- Docker runs the app with **gunicorn** and binds to **port 7860** (or `$PORT` if provided by the host).

=======
>>>>>>> d6832e31e439072de081850002c54f6902723475
## Tech Stack

- **Backend**: Flask (Python)
- **ML / NLP**: scikit-learn, numpy, joblib, TF-IDF + SVC
- **Templates / Static**: Jinja2, HTML, CSS
- **Serving**: gunicorn inside a Docker container

## Local Setup (Without Docker)

1. **Create and activate a virtual environment** (optional but recommended).
2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the app**:

```bash
python app.py
```

<<<<<<< HEAD
4. Open `http://127.0.0.1:7860` in your browser.
=======
4. Open `http://127.0.0.1:5000` in your browser.
>>>>>>> d6832e31e439072de081850002c54f6902723475

## Docker Usage

1. **Build the image** (from the project root):

```bash
docker build -t text-detection-app .
```

2. **Run the container**:

```bash
<<<<<<< HEAD
docker run -p 7860:7860 text-detection-app
```

3. Open `http://127.0.0.1:7860` and use the web UI to test the text detection model.
=======
docker run -p 5000:5000 text-detection-app
```

3. Open `http://127.0.0.1:5000` and use the web UI to test the text detection model.
>>>>>>> d6832e31e439072de081850002c54f6902723475

##### Live at :

  https://zainch12.pythonanywhere.com/

<<<<<<< HEAD
##### Live demo (Hugging Face Spaces):

  https://huggingface.co/spaces/Zainch032/Text-Detection


#### Folder Structure :
    
    ├── app.py
    ├── model/
    │   ├── svc.pkl
    │   └── tfidf_vectorizer.pkl
    ├── static/
    │   └── style.css
    ├── templates/
    │   └── index.html
    ├── requirements.txt
    ├── Dockerfile
    ├── notebooks/
    │   └── model_training.ipynb
    └── data/  (ignored by git)
=======

#### Folder Structure :
    
    ├── app/                       
│   ├── model/                   
│   │   ├── svc.pkl           
│   │   └── tfidf_vectorizer.pkl 
│   ├── static/styles.css     
│   ├── templates/index.html    
│   ├── requirements.txt       
│   └── app.py                 
├── data/                      
│   ├── dataset.csv            
│   └── training_data.csv     
├── notebooks/                  
│   └── model_training.ipynb   
└── deployment_link
>>>>>>> d6832e31e439072de081850002c54f6902723475

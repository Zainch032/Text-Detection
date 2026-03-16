---
title: Text Detection
emoji: ⚡
colorFrom: yellow
colorTo: gray
sdk: docker
pinned: false
---

## Text Detection NLP App

This project is an end-to-end NLP pipeline for hate/offensive language detection. It includes **data cleaning**, **exploratory data analysis (EDA)**, **model training**, and **deployment of an NLP classifier** as a web app.

## Features

- **Data cleaning**: text normalization (lowercasing, punctuation/whitespace handling, basic noise removal).
- **EDA**: label distribution, text length exploration, and qualitative inspection of examples to understand the dataset.
- **Modeling**: TF-IDF vectorization with an SVC classifier (serialized with `joblib` and loaded at inference time).
- **Web UI**: simple Flask interface where users can input text and get predictions (Hate Speech, Offensive Language, Neither).
- **Deployment ready**: containerized with Docker for reproducible deployment.

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

4. Open `http://127.0.0.1:5000` in your browser.

## Docker Usage

1. **Build the image** (from the project root):

```bash
docker build -t text-detection-app .
```

2. **Run the container**:

```bash
docker run -p 5000:5000 text-detection-app
```

3. Open `http://127.0.0.1:5000` and use the web UI to test the text detection model.

##### Live at :

  https://zainch12.pythonanywhere.com/


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

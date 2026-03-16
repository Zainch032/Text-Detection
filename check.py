from huggingface_hub import HfApi
import os

api = HfApi()
token = os.environ.get("HF_TOKEN")

print("Uploading svc.pkl...")
api.upload_file(
    path_or_fileobj="C:/Users/Zainch-032/Text-Detection/model/svc.pkl",
    path_in_repo="model/svc.pkl",
    repo_id="Zainch032/Text-Detection",
    repo_type="space",
    token=token
)
print("svc.pkl done!")

print("Uploading tfidf_vectorizer.pkl...")
api.upload_file(
    path_or_fileobj="C:/Users/Zainch-032/Text-Detection/model/tfidf_vectorizer.pkl",
    path_in_repo="model/tfidf_vectorizer.pkl",
    repo_id="Zainch032/Text-Detection",
    repo_type="space",
    token=token
)
print("tfidf_vectorizer.pkl done!")

print("Verifying...")
files = api.list_repo_files(
    repo_id="Zainch032/Text-Detection",
    repo_type="space",
    token=token
)
for f in files:
    if "model" in f:
        print(f"Found: {f}")
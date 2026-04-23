import pickle
import os
from fastapi import FastAPI

app = FastAPI()

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

model_dir = os.path.join(BASE_DIR, "models")

# Find latest model
model_files = [f for f in os.listdir(model_dir) if f.endswith(".pkl")]
model_files.sort(reverse=True)

latest_model = os.path.join(model_dir, model_files[0])

model = pickle.load(open(latest_model, "rb"))

print(f"Loaded model: {latest_model}")


@app.get("/")
def home():
    return {"status": "Prediction API running"}
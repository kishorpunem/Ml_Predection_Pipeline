import pickle
import os
from datetime import datetime

def save_model(model):

    os.makedirs("models", exist_ok=True)

    # create version using timestamp
    version = datetime.now().strftime("%Y%m%d_%H%M%S")

    model_path = f"models/model_{version}.pkl"

    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved successfully: {model_path}")
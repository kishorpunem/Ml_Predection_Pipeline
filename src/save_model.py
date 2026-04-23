import pickle

def save_model(model):

    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model saved successfully")
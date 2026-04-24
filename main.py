from src.data_ingestion import load_json
from src.data_cleaning import clean_data
from src.feature_engineering import feature_engineering
from src.train_model import train_model
from src.save_model import save_model


def run_pipeline():
    df = load_json()
    df = clean_data(df)
    df = feature_engineering(df)
    model = train_model(df)
    save_model(model)


if __name__ == "__main__":
    run_pipeline()
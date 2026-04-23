import pandas as pd

def load_json():

    df = pd.read_json("data/raw/Inquiry.OrderMasterone.json")

    print("Data Loaded")
    print(df.head())

    return df
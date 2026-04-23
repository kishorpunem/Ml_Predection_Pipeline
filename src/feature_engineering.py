import pandas as pd

def feature_engineering(df):

    selected_columns = [
        "ratePerAsset",
        "transportType",
        "moveType",
        "commodity",
        "loadingType",
        "totalGrossWeight",
        "clientCategory"
    ]

    df = df[selected_columns]

    df = pd.get_dummies(df)

    return df
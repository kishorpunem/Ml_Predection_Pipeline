import numpy as np
import os

def clean_data(df):

    # Extract MongoDB ObjectId
    if "_id" in df.columns:
        df["_id"] = df["_id"].apply(
            lambda x: x.get("$oid") if isinstance(x, dict) else x
        )

    df.replace(["", "NA", "null"], np.nan, inplace=True)

    if "_id" in df.columns:
        df.drop_duplicates(subset="_id", inplace=True)

    df.ffill(inplace=True)

    # Save cleaned data
    os.makedirs("data/clean_data", exist_ok=True)
    df.to_csv("data/clean_data/clean_data.csv", index=False)

    print("Clean data saved to data/clean_data/clean_data.csv")

    return df
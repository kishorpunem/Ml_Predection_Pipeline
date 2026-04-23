from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from src.utils.logger import logger

def train_model(df):

    y = df["ratePerAsset"]
    X = df.drop("ratePerAsset", axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor()

    logger.info("Training started")

    model.fit(X_train, y_train)

    logger.info("Training completed successfully")

    print("Model trained successfully")

    return model
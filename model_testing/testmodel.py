import pickle
import os
import pandas as pd
import json
from sklearn.metrics import mean_squared_error, r2_score

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Find latest model automatically
model_dir = os.path.join(BASE_DIR, "models")

model_files = [f for f in os.listdir(model_dir) if f.endswith(".pkl")]
model_files.sort(reverse=True)

latest_model = model_files[0]

model_path = os.path.join(model_dir, latest_model)

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

print(f"Model loaded successfully: {latest_model}")

data_path = os.path.join(BASE_DIR, "data", "clean_data", "clean_data.csv")

# Load model
with open(model_path, "rb") as f:
    model = pickle.load(f)

print("Model loaded successfully")

# Load dataset
df = pd.read_csv(data_path)

target_column = "ratePerAsset"

# Example identifier fields
id_columns = ["inquiryNumber", "orderNumber","orderStatus"]

# Save ID values separately
id_data = df[id_columns].head(20)

# Features for prediction
X = df.drop(columns=[target_column] + id_columns, errors="ignore")
y = df[target_column]

# Convert categorical features
X = pd.get_dummies(X)

# Align features
expected_features = model.feature_names_in_

for col in expected_features:
    if col not in X.columns:
        X[col] = 0

X = X[expected_features]

X_test = X.head(20)
y_test = y.head(20)

# Predict
predictions = model.predict(X_test)

# Build JSON output
results = []

for i in range(len(predictions)):
    results.append({
        "orderId": str(id_data.iloc[i]["inquiryNumber"]),
        "lineItemId": str(id_data.iloc[i]["orderNumber"]),
        "OrderStatus": str(id_data.iloc[i]["orderStatus"]),
        "predictedRatePerAsset": float(predictions[i]),
        "actualRatePerAsset": float(y_test.iloc[i])
    })

output = {
    "modelType": str(type(model)),
    "predictionResults": results
}

print(json.dumps(output, indent=4))
from google.cloud import storage

def upload_model():

    project_id = "project-f95eec44-2dc1-463f-b7f"
    bucket_name = "kishor-ml-model-storage"
    source_file = "C:/Users/kisho/PycharmProjects/Ml_Prediction_pipeline/models/model.pkl"
    destination_blob = "models/model.pkl"

    client = storage.Client(project=project_id)

    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)

    blob.upload_from_filename(source_file)

    print("Model uploaded successfully")


upload_model()
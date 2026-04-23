import os
from google.cloud import storage


def upload_model():

    project_id = "project-f95eec44-2dc1-463f-b7f"
    bucket_name = "kishor-ml-model-storage"

    # Get project root directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Correct models path
    model_dir = os.path.join(BASE_DIR, "models")

    # Find latest model
    model_files = [f for f in os.listdir(model_dir) if f.endswith(".pkl")]
    model_files.sort(reverse=True)

    latest_model = model_files[0]

    source_file = os.path.join(model_dir, latest_model)
    destination_blob = f"models/{latest_model}"

    client = storage.Client(project=project_id)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob)

    blob.upload_from_filename(source_file)

    print(f"Uploaded latest model: {latest_model}")


upload_model()
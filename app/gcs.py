from google.cloud import storage
import uuid

def upload_image_to_bucket(file, bucket_name: str) -> str:
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    # Generar un nombre único
    blob_name = f"{uuid.uuid4()}-{file.filename}"
    blob = bucket.blob(blob_name)
    
    blob.upload_from_file(file.file, content_type=file.content_type)
    blob.make_public()
    
    return blob.public_url

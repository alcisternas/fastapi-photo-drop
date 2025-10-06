from fastapi import FastAPI, File, UploadFile, HTTPException
from app.gcs import upload_image_to_bucket

app = FastAPI(title="Photo Drop", version="1.0.0")

# Configuración del bucket (puedes usar una variable de entorno)
BUCKET_NAME = "photo-drop-bucket-ac"

@app.get("/")
def root():
    return {"message": "Bienvenido a Photo Drop!"}

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Solo imágenes por favor.")

    try:
        public_url = upload_image_to_bucket(file, BUCKET_NAME)
        return {"url": public_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 📸 Photo Drop – DevOps + FastAPI + Cloud Run

**Photo Drop** es una API web hecha con **FastAPI** que permite a los usuarios subir imágenes a un bucket de **Google Cloud Storage**. 

- ⚙️ Docker
- 🧪 Jenkins (CI/CD)
- ☁️ Google Cloud Run
- 🗄️ Google Cloud Storage

---

## 📦 Funcionalidad

- 📤 Sube imágenes al bucket `photo-drop-bucket` en GCS
- 🔗 Retorna una URL pública para cada imagen
- 🔒 Valida que el archivo sea una imagen
- 🔁 Despliegue automatizado con Jenkins + Cloud Run
- 🌍 API documentada con Swagger en `/docs`

---

## 🚀 Tecnologías Usadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Docker](https://www.docker.com/)
- [Google Cloud Storage](https://cloud.google.com/storage)
- [Google Cloud Run](https://cloud.google.com/run)
- [Jenkins](https://www.jenkins.io/)

---

## 📁 Estructura del Proyecto

├── app
│ ├── main.py # API principal
│ └── gcs.py # Función para subir imágenes a GCS
├── requirements.txt # Dependencias de Python
├── Dockerfile # Imagen Docker
├── Jenkinsfile # Pipeline CI/CD
└── README.md # Este archivo

## 📁 Endpoints

| Método | Ruta       | Descripción                       |
| ------ | ---------- | --------------------------------- |
| GET    | `/`        | Mensaje de bienvenida             |
| GET    | `/healthz` | Health check                      |
| POST   | `/upload`  | Sube imagen a GCS y retorna URL   |
| GET    | `/docs`    | Documentación Swagger interactiva |


## 📁 Buckets y permisos

- gsutil mb -l southamerica-west1 gs://photo-drop-bucket
- gsutil iam ch allUsers:objectViewer gs://photo-drop-bucket


🧱 Requisitos

Antes de comenzar, asegúrate de tener:

- ✅ Una cuenta de Google Cloud
- ✅ Un bucket creado (photo-drop-bucket)
- ✅ Jenkins configurado con un agente y acceso a tu repositorio
- ✅ Un Service Account con permisos adecuados
- ✅ Habilitado: Cloud Run API, Artifact Registry, Cloud Storage, IAM
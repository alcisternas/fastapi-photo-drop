pipeline {
  agent any

  environment {
    REGION        = 'us-central1'
    REPO_NAME     = 'apps'
    SERVICE_NAME  = 'fastapi-bucket'
    PROJECT_ID    = 'possible-sun-471215-d3'
    REGISTRY_HOST = "${REGION}-docker.pkg.dev"
  }

  options {
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('GCloud Auth') {
      steps {
        withCredentials([file(credentialsId: 'gcp-sa-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
          sh '''
            gcloud auth activate-service-account --key-file="$GOOGLE_APPLICATION_CREDENTIALS"
            gcloud config set project ${PROJECT_ID}
            gcloud auth configure-docker ${REGISTRY_HOST} -q
          '''
        }
      }
    }

    stage('Build & Push Image') {
      steps {
        script {
          def COMMIT = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
          env.IMAGE = "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${SERVICE_NAME}:${COMMIT}"
          env.IMAGE_LATEST = "${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/${SERVICE_NAME}:latest"
        }
        sh '''
          docker build -t "${IMAGE}" -t "${IMAGE_LATEST}" .
          docker push "${IMAGE}"
          docker push "${IMAGE_LATEST}"
        '''
      }
    }

    stage('Deploy to Cloud Run') {
      steps {
        sh '''
          gcloud run deploy ${SERVICE_NAME} \
            --image ${IMAGE} \
            --platform managed \
            --region ${REGION} \
            --allow-unauthenticated \
            --port 8000
        '''
      }
    }

    stage('Smoke Test') {
      steps {
        sh '''
          URL=$(gcloud run services describe ${SERVICE_NAME} --region=${REGION} --format='value(status.url)')
          echo "Haciendo smoke test contra $URL/docs"
          curl -fsS "$URL/docs" || exit 1
        '''
      }
    }
  }

  post {
    success {
      script {
        def url = sh(returnStdout: true, script: "gcloud run services describe ${SERVICE_NAME} --region ${REGION} --format='value(status.url)'").trim()
        echo "✅ Despliegue OK: ${url}"
      }
    }
    failure {
      echo '❌ Falló el pipeline. Revisa los logs (auth, permisos, build, deploy).'
    }
  }
}

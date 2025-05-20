pipeline {
  agent any

  environment {
    DOCKER_HUB_CREDENTIALS = credentials('docker-hub-creds') // create this in Jenkins
    IMAGE_NAME = "shivamsinha2000/flask-app:latest"
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/shivamsinha2000/AutoRes.git', branch: 'main'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          docker.build("${IMAGE_NAME}")
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        script {
          docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-creds') {
            docker.image("${IMAGE_NAME}").push()
          }
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f flask-deployment.yaml'
        sh 'kubectl apply -f flask-service.yaml'
      }
    }
  }
}





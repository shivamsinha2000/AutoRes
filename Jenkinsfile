pipeline {
    agent any

    environment {
        IMAGE_NAME = "shivamsinha2000/flask-app"
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
                    bat "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        bat """
                        docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                        docker push ${IMAGE_NAME}:latest
                        """
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    bat 'kubectl apply -f flask-deployment.yaml'
                    bat 'kubectl apply -f flask-service.yaml'
                    bat 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}

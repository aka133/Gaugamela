pipeline {
    agent any
    
    environment {
        DOCKER_REGISTRY = '192.168.86.39:30500'
        IMAGE_NAME = 'gaugamela'

    }

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:latest'
            }
        }

        stage('Push') {
            steps {
                sh 'docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:latest'
            }
        }

        stage('Deploy') {
            steps {
                sh 'kubectl apply -f kubernetes/deployment.yaml'
                sh 'kubectl rollout restart deployment gaugamela'
            }
        }
    }

}
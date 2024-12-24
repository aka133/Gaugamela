pipeline {
    agent any
    
    environment {
        REGISTRY = '192.168.86.39:30500'
        IMAGE_NAME = 'gaugamela'
    }
    
    stages {
        stage('Build and Push') {
            steps {
                sh '''
                    # Build using docker
                    docker build -t ${REGISTRY}/${IMAGE_NAME}:latest .
                    docker push ${REGISTRY}/${IMAGE_NAME}:latest
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh '''
                    kubectl apply -f kubernetes/deployment.yaml
                    kubectl rollout restart deployment gaugamela
                '''
            }
        }
    }
}
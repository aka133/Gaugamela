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
                    # Use k3s crictl commands instead of docker
                    k3s crictl build -t ${REGISTRY}/${IMAGE_NAME}:latest .
                    k3s crictl push ${REGISTRY}/${IMAGE_NAME}:latest
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'k3s kubectl apply -f kubernetes/deployment.yaml'
                sh 'k3s kubectl rollout restart deployment gaugamela'
            }
        }
    }
}
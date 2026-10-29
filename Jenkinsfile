pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install & Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t eco-footprint-calculator:latest .'
            }
        }

        stage('Run & Test Docker Container') {
            steps {
                sh 'echo -e "10\n150\n5" | docker run --rm -i eco-footprint-calculator:latest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                // Securely injects credentials using the ID you created in Jenkins
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        // Log in to Docker Hub securely via stdin
                        sh "echo '${DOCKER_PASS}' | docker login -u '${DOCKER_USER}' --password-stdin"
                        
                        // Tag the local image for your Docker Hub repository
                        sh 'docker tag eco-footprint-calculator:latest 02fe25bca004/eco-footprint-calculator:latest'
                        
                        // Push the image to Docker Hub
                        sh 'docker push 02fe25bca004/eco-footprint-calculator:latest'
                    }
                }
            }
        }
    }
}
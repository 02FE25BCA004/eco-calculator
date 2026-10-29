pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Pulls code from your GitHub repository
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
                script {
                    // Builds the Docker container image
                    docker.image('eco-footprint-calculator:latest').build('.')
                }
            }
        }
    }
}
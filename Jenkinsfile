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
                // Uses a direct docker build command via shell
                sh 'docker build -t eco-footprint-calculator:latest .'
            }
        }
    }
}
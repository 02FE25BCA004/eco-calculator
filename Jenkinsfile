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
                sh '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t eco-footprint-calculator:latest .'
            }
        }

        stage('Run Container (Pre-Fed Values)') {
            steps {
                // Runs headlessly with pre-fed values baked into python script
                sh '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" run --rm eco-footprint-calculator:latest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh "echo '${DOCKER_PASS}' | \"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe\" login -u '${DOCKER_USER}' --password-stdin"
                        sh '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" tag eco-footprint-calculator:latest 02FE25BCA004/eco-footprint-calculator:latest'
                        sh '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" push 02FE25BCA004/eco-footprint-calculator:latest'
                    }
                }
            }
        }
    }
}
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
                // Uses the absolute path to Docker on Windows
                sh '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" build -t eco-footprint-calculator:latest .'
            }
        }

        stage('Run & Test Docker Container') {
            steps {
                sh 'echo -e "10\n150\n5" | "C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" run --rm -i eco-footprint-calculator:latest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh "echo '${DOCKER_PASS}' | \"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe\" login -u '${DOCKER_USER}' --password-stdin"
                        
                        // Using your GitHub/Docker Hub username: 02FE25BCA004
                        sh '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" tag eco-footprint-calculator:latest 02FE25BCA004/eco-footprint-calculator:latest'
                        sh '"C:\\Program Files\\Docker\\Docker\\resources\\bin\\docker.exe" push 02FE25BCA004/eco-footprint-calculator:latest'
                    }
                }
            }
        }
    }
}
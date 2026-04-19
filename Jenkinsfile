pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-app .'
            }
        }

        stage('Run Tests') {
            steps {
                echo "Tests go here"
            }
        }
    }
}


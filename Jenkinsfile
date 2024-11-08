pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/username/demo3.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the project...'
            }
        }
    }
}

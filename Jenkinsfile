pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Check Python Version') {
            steps {
                bat 'C:/Users/Milana/AppData/Local/Programs/Python/Python313/python.exe --version'
            }
        }
        stage('Setup Python') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                pytest --junitxml=report.xml
                '''
            }
        }
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'report.xml', fingerprint: true
            }
        }
    }
}

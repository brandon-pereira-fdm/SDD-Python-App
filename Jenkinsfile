pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest -v'
            }
        }

        stage('Package') {
            steps {
                sh '''
                    zip -r sdd-python-webapp.zip \
                    app.py \
                    templates \
                    tests \
                    requirements.txt \
                    README.md
                '''
            }
        }

        stage('Archive Artifact') {
            steps {
                archiveArtifacts artifacts: 'sdd-python-webapp.zip', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Build successful. The SDD Python web app passed tests and was packaged.'
        }

        failure {
            echo 'Build failed. Check the console output and fix the failing stage.'
        }
    }
}
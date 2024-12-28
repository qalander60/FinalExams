pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}\\env"  // Use backslashes for Windows paths
        REQUIREMENTS_FILE = "requirements.txt"
        APP_ENTRY = "app.py"  // Entry point of the Flask app
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/qalander60/FinalExams.git'  // Replace with your repo URL
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                ${VENV_DIR}\\Scripts\\activate
                pip install --upgrade pip
                if exist ${WORKSPACE}\\${REQUIREMENTS_FILE} (
                    pip install -r ${WORKSPACE}\\${REQUIREMENTS_FILE}
                )
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '''
                ${VENV_DIR}\\Scripts\\activate
                pytest --maxfail=1 --disable-warnings
                '''
            }
        }

        stage('Build the App') {
            steps {
                bat '''
                ${VENV_DIR}\\Scripts\\activate
                python -m flask --version
                '''
            }
        }

        stage('Deploy the App') {
            steps {
                bat '''
                ${VENV_DIR}\\Scripts\\activate
                start /B python ${WORKSPACE}\\${APP_ENTRY} > app.log 2>&1
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}

pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/env" // Use the existing 'env' directory
        REQUIREMENTS_FILE = "requirements.txt"
        APP_ENTRY = "app.py" // Entry point of the Flask app
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/qalander60/FinalExams.git' // Replace with your repo URL
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                if [ -f ${WORKSPACE}/${REQUIREMENTS_FILE} ]; then
                    pip install -r ${WORKSPACE}/${REQUIREMENTS_FILE}
                fi
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                pytest --maxfail=1 --disable-warnings
                '''
            }
        }

        stage('Build the App') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                python -m flask --version
                '''
            }
        }

        stage('Deploy the App') {
            steps {
                sh '''
                source ${VENV_DIR}/bin/activate
                nohup python ${WORKSPACE}/${APP_ENTRY} > app.log 2>&1 &
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

pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    environment {
        STUDENT_NAME = 'Daniyar'
        STUDENT_SURNAME = 'Namet'
        STUDENT_GROUP = 'IT2-2312 SE'
        STUDENT_ID = '37056'

        IMAGE_NAME = 'namet-daniyar-devops'
        CONTAINER_NAME = 'namet-daniyar-container'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m compileall -q app'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s app -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t "$IMAGE_NAME:latest" .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f "$CONTAINER_NAME" 2>/dev/null || true

                    docker run -d \
                        --name "$CONTAINER_NAME" \
                        -p 8080:8080 \
                        -e STUDENT_NAME="$STUDENT_NAME" \
                        -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                        -e STUDENT_GROUP="$STUDENT_GROUP" \
                        -e STUDENT_ID="$STUDENT_ID" \
                        "$IMAGE_NAME:latest"

                    docker ps --filter "name=$CONTAINER_NAME"
                    docker logs "$CONTAINER_NAME"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
            echo "Student: ${env.STUDENT_NAME} ${env.STUDENT_SURNAME}"
            echo "Group: ${env.STUDENT_GROUP}"
            echo "Student ID: ${env.STUDENT_ID}"
        }

        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }
    }
}

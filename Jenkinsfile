pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                git 'https://github.com/sumitkumar74604/NCS_folder.git'
            }
        }
        stage('deploy') {
            steps {
                script {
                    // Ensure docker-compose commands are executed without sudo if possible
                    sh '''
                    docker-compose down
                    docker-compose up -d
                    '''
                }
            }
        }
    }
}

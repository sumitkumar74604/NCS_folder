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
                sh '''#!bin/bash
                    sudo docker-compose down
                    sudo docker-compose up -d'''
            }
        }
    }
}

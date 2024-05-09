// 


pipeline {
    agent any
    
    stages {
        
        stage("code"){
            steps{
                git url: "https://github.com/gehlotdeep/Github_Actions_ncs.git"
                echo 'Code Cloning'
            }
        }
        stage("build"){
            steps{
                sh "docker build -t django-image ."
                echo 'code builded'
            }
        }
        stage("scan image"){
            steps{
                echo 'image scanning'
            }
        }
        stage("push image DockerHub"){
            steps{
                withCredentials([usernamePassword(credentialsId:"dockerhub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker tag django-image:latest ${env.dockerHubUser}/django-image:latest"
                sh "docker push ${env.dockerHubUser}/django-image:latest"
                echo 'image pushed'
                }
            }
        }
        stage("deploy"){
            steps{
                sh "docker-compose down && docker-compose up -d"
                echo 'deployment'
            }
        }
    }
}
// 


pipeline {
    agent any
    
    stages {
        
        stage("code"){
            steps{
                git url: "https://github.com/gehlotdeep/Github_Actions_ncs.git", branch: "main"
                echo 'Code Cloning'
            }
        }
        stage("build and test"){
            steps{
                sh "docker build -t ncs-image ."
                echo 'code builded'
            }
        }
        stage("scan image"){
            steps{
                echo 'image scanning'
            }
        }
        stage("push"){
            steps{
                withCredentials([usernamePassword(credentialsId:"dockerhub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                sh "docker tag ncs-image:latest ${env.dockerHubUser}/ncs-image:latest"
                sh "docker push ${env.dockerHubUser}/ncs-image:latest"
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
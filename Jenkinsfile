pipeline{
    agent any
    stages{
        stage("code download and software download"){
            steps{
                sh 'wget https://github.com/Asp2591/Jenkins-Poll-scm-test.git'
                sh 'sudo yum update -y && sudo yum upgrade -y'
                sh 'sudo yum install docker -y'
                sh 'sudo systemctl start docker'
                sh 'sudo systemctl enable docker'
            }
        }
        stage("building docker image"){
            steps{
                git branch:'main',url:'https://github.com/Asp2591/Jenkins-Poll-scm-test.git'
                sh 'sudo docker build -t helloworld-devops:latest .'
            }
        }
        stage("running website"){
            steps{
                sh 'sudo docker run -d -p 8181:8181 helloworld-devops:latest'
            }
        }
        
    }
}

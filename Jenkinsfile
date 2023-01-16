pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh "docker stop weddingsite_container"
                sh "docker rm weddingsite_container"
                sh "docker rmi theearlofgray/weddingsite:latest"
                sh "docker build -t theearlofgray/weddingsite:latest ."
                sh "docker push theearlofgray/weddingsite:latest"
                
            }
        }
        stage('Deploy') {
            steps {
                sh "docker run -d -p 5000:5000 --name weddingsite_container theearlofgray/weddingsite:latest"
            }
        }
    }
}
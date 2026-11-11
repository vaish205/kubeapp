pipeline{
    agent any
    stages{
        stage('Build docker image'){
            steps{
                echo 'Building docker image...'
                bat 'docker build -t myapp1 .'
            }
        }
        stage('docker login'){
            steps{
                echo 'Logging into docker registry'
                bat 'docker login -u vaish205 -p Tejuvaishu@2005'
            }
        }
        stage('Push docker image'){
            steps{
                echo 'Pushing docker image'
                bat 'docker tag myapp1 vaish205/sample1:latest'
                bat 'docker push vaish205/sample1:latest'
            }
        }
        stage('Deploy to Kubernetes'){
            steps{
                echo 'Deploying to Kubernetes...'
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
        success{
            echo 'Pipeline completed successfully!'
        }
        failure{
            echo 'Pipeline failed!'
        }
    }
}

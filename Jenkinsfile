pipeline {
    agent any
    
    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    } 
    stages {
        stage('Git') {
            steps {
                script {
                    def repoDir = 'trabalho-devops-2290724'
                    if (fileExists(repoDir)) {
                        echo "Repository already exists. Pulling latest changes."
                        sh "rm -rf ${repoDir}"
                        sh 'git clone https://github.com/ElcioAngelo/trabalho-devops-2290724.git'
                    } 
                    dir(repoDir) {
                        sh 'git checkout main'
                    }
                }
            }
        }
        stage('test') {
            steps {
                script {
                    sh '''
                    docker compose up mariadb
                    sleep 10 
                    docker compose up flask
                    '''
                }
            }
        }
        stage('Build') { 
            steps {
                script {
                    echo "Running docker compose commands"
                    
                    sh '''
                        docker container prune
                        docker compose down
                        docker compose up --build
                    '''  
                }
            }
        } 
    }
}
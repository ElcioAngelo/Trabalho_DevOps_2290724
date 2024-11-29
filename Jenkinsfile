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
                        dir(repoDir) {
                            sh 'git pull origin main'
                        }
                    } else {
                        echo "Cloning repository."
                        sh 'git clone https://github.com/ElcioAngelo/trabalho-devops-2290724.git'
                    }
                    
                    dir(repoDir) {
                        sh 'git checkout main'
                    }
                }
            }
        }
        stage('Build') { 
            steps {
                script {
                    echo "Running docker compose commands"
                    
                    sh '''
                        docker compose down
                        docker compose up --build
                    '''  
                }
            }
        } 
        stage('Test') {
            steps{
                script {
                    sh 'cd test && pip install -r requirements.txt'
                    sh 'python3 test.py'  
                }
            }
        }
    }
}
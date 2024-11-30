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
        stage('Test') {
            steps{
                script {
                    sh 'docker compose up --build -d mariadb_container'
                    sh 'sleep(time: 10, unit: 'SECONDS')'
                    sh 'docker compose up --build -d flaskapp_container'
                    sh 'sleep(time: 10, unit: 'SECONDS')'                    
                    sh 'cd test && pip install -r requirements.txt'
                    sh 'python3 test.py'  
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
    }
}
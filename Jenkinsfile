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
            steps {
                script {
                    // Start the containers in detached mode with build
                    sh 'docker compose up --build'

                    // Optional: Sleep for a fixed time to allow the containers to initialize
                    echo 'Sleeping for 10 seconds to allow containers to initialize...'
                    sleep(time: 10, unit: 'SECONDS')

                    //Execution of the test.
                    sh 'docker exec flaskapp_container python /app/test.py'
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
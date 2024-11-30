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

                    // Wait for the Flask and MariaDB containers to be accessible (Check if the ports are open)
                    echo 'Checking if containers are accessible...'
                    def containersReady = false
                    timeout(time: 60, unit: 'SECONDS') {
                        // Check if the Flask and MariaDB containers' ports are open
                        while (!containersReady) {
                            // Checking if Flask container is accepting connections on port 5000
                            def flaskStatus = sh(script: "docker exec mariadb_container nc -zv localhost 3306", returnStatus: true)
                            def dbStatus = sh(script: "docker exec flaskapp_container nc -zv localhost 5000", returnStatus: true)

                            // If both ports are open, containers are ready
                            if (flaskStatus == 0 && dbStatus == 0) {
                                containersReady = true
                                echo 'Containers are up and accepting connections on their respective ports!'
                            } else {
                                echo 'Waiting for containers to be accessible on their ports...'
                                sleep(time: 5, unit: 'SECONDS')
                            }
                        }
                    }

                    // Install dependencies for testing
                    sh 'cd test && pip install -r requirements.txt'

                    // Execute the tests
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
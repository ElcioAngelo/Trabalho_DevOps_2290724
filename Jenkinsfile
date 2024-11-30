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
                    sh 'docker compose up -d --build'

                    // Optional: Sleep for a fixed time to allow the containers to initialize
                    echo 'Sleeping for 10 seconds to allow containers to initialize...'
                    sleep(time: 10, unit: 'SECONDS')

                    // Check if the containers are up and ready (using docker inspect for health status)
                    echo 'Checking if containers are up and ready...'
                    def containersReady = false
                    timeout(time: 60, unit: 'SECONDS') {
                        // Wait until the containers are ready
                        while (!containersReady) {
                            def flaskStatus = sh(script: "docker inspect -f '{{.State.Health.Status}}' flaskapp_container", returnStdout: true).trim()
                            def dbStatus = sh(script: "docker inspect -f '{{.State.Health.Status}}' mariadb_container", returnStdout: true).trim()

                            // Assuming that the containers have health checks defined
                            if (flaskStatus == 'healthy' && dbStatus == 'healthy') {
                                containersReady = true
                                echo 'Containers are ready!'
                            } else {
                                echo 'Waiting for containers to be healthy...'
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
#!/bin/bash

# Run the tests first
echo "Checking if mariadb container is up and available.."
/app/wait-for-it.sh mariadb_container:3306 --timeout=10 --strict -- echo "MariaDB is up"
echo "Running tests with pytest..."
pytest app_test.py 

# Check if pytest passed (exit code 0 means tests passed)
if [ $? -eq 0 ]; then
  echo "Tests passed. Starting Flask app..."
  # Run the Flask app
  flask run --host=0.0.0.0
else
  echo "Tests failed. Not starting Flask app."
  exit 1
fi

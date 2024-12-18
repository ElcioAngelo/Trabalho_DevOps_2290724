#!/bin/bash

# Run the tests first
echo "Running tests with pytest..."
pytest app_test.py 

#Waits 5 seconds for the mariaDB initialization.
sleep 5

#verifies if the test was sucessfull or not.
if [ $? -eq 0 ]; then
  echo "Tests passed. Starting Flask app..."
  # Run the Flask app
  flask run --host=0.0.0.0
else
  echo "Tests failed. Not starting Flask app."
  exit 1
fi

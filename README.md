# Face-Service
Providing Face Recognition as a Service for easy integration of Face recognition into Authentication

## Usage

Create an uploads folder in root directory

If docker is installed Simply run `docker-compose up`

If not installed Run 
` chmod +x run.sh
  ./run.sh `
And in new terminal run a simple file server eg: `http-server` or `python -m SimpleHTTPServer`

Then make a POST Request to /add to insert images (This step will return an id store it) <br/>
Then make a POST Request to /detect to detect faces with new face as form data with key file and value the face image file and the id which was returned in previous step.

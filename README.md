# Project-Mentor-API
## In this repository located an API, whichs connects aspiring programmers with experienced teachers (programmers). API include authorization and authentication on JWT based. Thanks to the API, aspiring and experienced programmers can create profile, where written information about them. The aspiring programmes can find the profils of experienced programmers and apply for a meeting.

# Starting the program
## You can start this programm in two ways:
1. On your local computer
    * Make sure you have Python version 3.10 installed, PostgreSQL and redis
    * Do git pull of this repository
    * Create a virtual environment (Optional)
    * Install the required dependencies with the command: ```pip install -r req.txt```
    * Create a .env file where these parameters will be:  
        * DB_HOST
        * DB_PORT
        * DB_USER
        * DB_PASS
        * DB_NAME
        * SECRET_AUTH_KEY
        * REDIS_HOST
        * EMAIL_LOGIN
        * EMAIL_PASSWORD  
    The last two parameters can be obtained here: [link](https://myaccount.google.com/)
    * Go to the app directory
    * Enter the command: ```uvicorn main:app --reload```
    * Go to the this URL: http://localhost:8000/docs, there you will see all endpoints of API

2. Via docker
    * Do git pull of this repository
    * Go to the project terminal
    * Enter the command: ```docker build .```
    * Then: ```docker compose up```
    * Go to the this URL: http://localhost:8000/docs, there you will see all endpoints of API
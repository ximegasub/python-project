# Final python-project
Basic Python Flask app in Docker which displays the time, date, timezone, hostname and ip address of the container

### Project structure
```
python-project/
├── src
│   ├── __init__.py
│   ├── app.py
|   └── data
│       └── details.json
├── tests
│   ├── __init__.py
│   ├── test_details.py
|   └── test_data.json
├── requirements.txt
├── test-requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .gitignore
├── .dockerignore
└── .env

```

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/ximegasub/python-project.git
$ git checkout xsubieta-final-project
$ docker-compose build
```

### Run docker compose
```
$ docker-compose up -d
```

Visit:
Python Application
-  http://localhost:8000/details
-  http://localhost:8000/list-details
Portainer
-  http://localhost:9001
Nexus:
-  http://localhost:8081
Jenkins:
-  http://localhost:8080
Sonarqube
-  http://localhost:9000  

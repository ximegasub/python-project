# python-project
Basic Python Flask app in Docker which displays the time, date, timezone, hostname and ip address of the container

### Project structure
```
python-project/
├── src
│   ├── __init__.py
│   ├── app.py
|   └── data
│       └── details.json
├── requirements.txt
└── Dockerfile
```

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/ximegasub/python-project.git
$ docker build --tag ximegasub/python-flask-docker:ximena.subieta .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/ximegasub/python-flask-docker).
```
docker pull ximegasub/python-flask-docker:ximena.subieta
```

### Run the container
Create a container from the image.
```
$ docker run -it --name <container name> -d -p 8000:8000 -v /python-project/data ximegasub/python-flask-docker:ximena.subieta
```

Visit http://localhost:8000/details:
```
{"date":"2022-07-18","hostname":"d4eb987b46e8","ip_address":{"eth0":["172.17.0.4"],"lo":["127.0.0.1"]},"time":"00:45:27","timezone":"Etc/UTC"} 
```
Also, visit http://localhost:8000/list-details to see all details.

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container name>
172.17.0.4
$ docker inspect -f '{{ .Config.Hostname }}' <container name>
d4eb987b46e8
```


FROM python:3.8-slim-buster
EXPOSE 8000
WORKDIR /python-project
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY src/ .
CMD ["flask", "run", "--port=8000", "--host=0.0.0.0"]

FROM python:3.8-slim-buster as build
WORKDIR /python-project
COPY . .
RUN pip3 install -r requirements.txt

FROM build
WORKDIR /python-project
RUN pip3 install -r test-requirements.txt \
    && pytest tests

FROM build
EXPOSE 8000
WORKDIR /python-project/src/
CMD ["flask", "run", "--port=8000", "--host=0.0.0.0"]

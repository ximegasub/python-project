FROM python:3.8-slim-buster as build
COPY . .
RUN pip3 install -r requirements.txt

FROM build
COPY test-requirements.txt test-requirements.txt && tests tests
RUN pip3 install -r test-requirements.txt && pytest tests

FROM build
EXPOSE 8000
COPY src .
CMD ["flask", "run", "--port=8000", "--host=0.0.0.0"]

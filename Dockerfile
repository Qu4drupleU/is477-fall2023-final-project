FROM python:3.10
WORKDIR /is477-fall2023-final-project
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

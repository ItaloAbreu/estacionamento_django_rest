FROM python:3.8

WORKDIR source/

COPY source/requirements.txt requirements.txt
COPY .env .env
RUN pip install -r requirements.txt

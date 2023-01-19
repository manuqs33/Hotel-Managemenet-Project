FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
RUN apt-get update

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
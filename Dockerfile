FROM python:3.10-slim

ENV PYTHONUNBUFFERED 1
RUN apt-get update

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/
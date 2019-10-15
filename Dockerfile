FROM python:3.7-buster


RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=true

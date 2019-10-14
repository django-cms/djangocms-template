FROM python:3.7-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code/
WORKDIR /code/
RUN pip install -r /code/requirements.txt

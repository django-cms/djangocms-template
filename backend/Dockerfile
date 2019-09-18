FROM python:3.7-stretch
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY requirements.txt /code/
RUN pip install -r /code/requirements.txt
COPY .. /code/
WORKDIR /code/

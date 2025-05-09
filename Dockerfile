# syntax=docker/dockerfile:1
FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app 
COPY requirements.txt /app/
RUN pip3 install --upgrade pip --timeout=600
RUN pip3  install -r requirements.txt
COPY ./core /app
#CMD [ "python", "manage.py","runserver","0.0.0.0:8000" ]

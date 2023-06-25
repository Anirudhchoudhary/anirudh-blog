FROM python:3.8


WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENV_TYPE "PROD"

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y certbot && apt-get install -y python3-certbot-nginx

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py migrate && gunicorn blobproject.wsgi:application --bind 0.0.0.0:8001
FROM python:3.8


WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENV_TYPE "PROD"
ENV MYSQL_PASSWORD Qwerty@12345
ENV MYSQL_DATABASE blog

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8001
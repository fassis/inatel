FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /var/www

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENTRYPOINT ["sh", "./docker/entrypoint.sh"]
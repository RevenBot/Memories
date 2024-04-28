FROM python:3.9-alpine

EXPOSE 8000

# env

ENV DJANGO_SUPERUSER_USERNAME admin
ENV DJANGO_SUPERUSER_PASSWORD admin

# Pipenv
RUN pip install --upgrade pip && \
    pip install pipenv

# Python dependencies
WORKDIR /memories
COPY . /memories
RUN pipenv install

# Web server
# https://gunicorn.org/
RUN pipenv install gunicorn

# Script
RUN chmod +x ./init.sh
RUN chmod +x ./manage.py

ENTRYPOINT ["./init.sh"]

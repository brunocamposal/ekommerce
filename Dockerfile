# image base
FROM python:3.8

# copy dependencies
COPY ./requirements.txt .

ENV PYTHONDONTWRITEBYTECODE 1

# install dependencies
RUN pip install -r requirements.txt

RUN apt update \
    && apt install -y libpq-dev gcc

RUN pip install psycopg2

# create folder app
WORKDIR /app

# create dependencies 
COPY . /app/
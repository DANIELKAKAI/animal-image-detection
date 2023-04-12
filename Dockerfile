# pull the official docker image
FROM python:3.10.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    libtiff-dev \
    libpng-dev \
    libwebp-dev \
    libaec-dev

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
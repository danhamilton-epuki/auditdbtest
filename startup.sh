#!/bin/bash
apt-get update
apt-get install -y --no-install-recommends \
    build-essential \
    unixodbc \
    unixodbc-dev \
    libssl-dev \
    libffi-dev \
    gcc g++

gunicorn -w 4 -b 0.0.0.0:8000 app:app

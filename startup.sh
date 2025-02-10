#!/bin/bash
apt-get update
apt-get install -y --no-install-recommends \
    build-essential \
    unixodbc \
    unixodbc-dev \
    libssl-dev \
    libffi-dev \
    gcc g++

pip install pyodbc --prefer-binary
pip install -r requirements.txt --no-cache-dir

gunicorn -w 4 -b 0.0.0.0:8000 app:app

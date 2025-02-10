#!/bin/bash
apt-get update
apt-get install -y unixodbc-dev gcc g++ build-essential libssl-dev
gunicorn -w 4 -b 0.0.0.0:8000 app:app

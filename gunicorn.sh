#!/bin/bash
sudo gunicorn -b localhost:8000 -w 4 main:app

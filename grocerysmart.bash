#!/usr/bin/env bash

# Check dependencies
echo "Verifying Dependencies"
pip install -r requirements.txt
echo "Dependencies Verified!"

# Start flask application
echo "Beginning flask application"
export flask_app=flask_scan.py
echo "Flask Application Started!"

# Begin Program
echo "Starting Server!"
python -m flask run
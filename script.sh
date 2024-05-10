#!/bin/bash

python3 ./main.py

if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. This is a requirement for the application. For a guide to install Python 3 please visit the following link https://realpython.com/installing-python/"
    exit 1
fi

if ! command -v pip3 &> /dev/null; then
    echo "Pip 3 is not installed. This is a requirement for the application, I will install it for you. For a guide to install Pip 3 manually, please see the README file. Alternatively, visit this link https://pypi.org/project/pip/"
exit 1
fi

python3 -m pip install --upgrade pip

python3 -m pip install -r ./src/requirements.txt

source .venv/bin/activate
python3 ./src/main.py
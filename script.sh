#!/bin/bash

if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'Error:
    Looks like you need to install pip3.
    To install pip3, please go to https://pypi.org/project/pip/' >&2
  exit 1
fi

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    Looks like Python3 is not installed.
    To install Python3, check out https://installpython3.com/' >&2
  exit 1
fi


cd ./src;

python3 -m venv .venv 
source .venv/bin/activate

pip3 install -r requirements.txt 

echo ""

echo ""
python3 main.py

deactivate

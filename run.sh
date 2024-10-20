#!/bin/bash

python -m venv .venv
source .venv/bin/activate
pip install -r src/requirements.txt
python src/app.py

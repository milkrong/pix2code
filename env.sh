#!/bin/bash

python3 -m venv ~/venv-pixcode
source ~/venv-pixcode/bin/activate
python -m pip install -U pip
python -m pip install Keras tensorflow opencv-python numpy
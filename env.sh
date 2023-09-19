#!/bin/bash

python3 -m venv ~/venv-metal
source ~/venv-metal/bin/activate
python -m pip install -U pip
python -m pip install Keras tensorflow opencv-python numpy
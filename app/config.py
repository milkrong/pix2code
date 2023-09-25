import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

TRAINED_MODEL_NAME = "pix2code"
TRAINED_MODEL_WEIGHTS = os.path.join(os.path.abspath(os.path.join(ROOT_DIR, os.pardir)), "bin")
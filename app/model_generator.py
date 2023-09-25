from .config import *
import numpy as np
from app.model.classes.model.pix2code import *

print(TRAINED_MODEL_WEIGHTS)
model = None
input_shape = None
output_size = None

def load_model():
    global input_shape 
    global output_size 
    global model
    meta_dataset = np.load("{}/meta_dataset.npy".format(TRAINED_MODEL_WEIGHTS))
    meta_dataset2 = np.load("{}/meta_dataset2.npy".format(TRAINED_MODEL_WEIGHTS))

    input_shape = meta_dataset2[0]
    output_size = meta_dataset[0]
    model = pix2code(input_shape, output_size, TRAINED_MODEL_WEIGHTS )
    model.load(TRAINED_MODEL_NAME)



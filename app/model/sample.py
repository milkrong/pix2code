import sys
import os

import numpy

from .classes.Sampler import *

from app.model_generator import model, input_shape, output_size
from app.config import TRAINED_MODEL_WEIGHTS

def sample_image(file):
    print(input_shape)
    sampler = Sampler(TRAINED_MODEL_WEIGHTS, input_shape, output_size, CONTEXT_LENGTH)
    # file_name = basename(input_path)[:basename(input_path).find(".")]
    evaluation_img = Utils.get_preprocessed_img(numpy.fromstring(file.read(), numpy.uint8), IMAGE_SIZE)

    print("Search with beam width: {}".format(3))
    result, _ = sampler.predict_beam_search(model, np.array([evaluation_img]), beam_width=3)
    print("Result beam: {}".format(result))

    return result

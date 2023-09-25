import sys
from os.path import join

import numpy

from .classes.Sampler import *
from .classes.model.pix2code import *
from ..main import ROOT_DIR

TRAINED_MODEL_NAME = "pix2code_model.h5"
TRAINED_MODEL_WEIGHTS = join(ROOT_DIR, "trained_models")

print(TRAINED_MODEL_WEIGHTS)


def sample_image(file):
    meta_dataset = np.load("{}/meta_dataset.npy".format(TRAINED_MODEL_WEIGHTS))
    meta_dataset2 = np.load("{}/meta_dataset2.npy".format(TRAINED_MODEL_WEIGHTS))
    input_shape = meta_dataset2[0]
    output_size = meta_dataset[0]

    model = pix2code(input_shape, output_size, )
    model.load(TRAINED_MODEL_NAME)

    sampler = Sampler(TRAINED_MODEL_WEIGHTS, input_shape, output_size, CONTEXT_LENGTH)

    # file_name = basename(input_path)[:basename(input_path).find(".")]
    evaluation_img = Utils.get_preprocessed_img(numpy.fromstring(file.read(), numpy.uint8), IMAGE_SIZE)

    print("Search with beam width: {}".format(3))
    result, _ = sampler.predict_beam_search(model, np.array([evaluation_img]), beam_width=3)
    print("Result beam: {}".format(result))

    return result

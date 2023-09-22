#!/usr/bin/env python
from __future__ import print_function
from __future__ import absolute_import

from os.path import join
from flask import app

import numpy
from classes.Sampler import *
from classes.model.pix2code import *

TRAINED_MODEL_NAME = "pix2code_model.h5"
TRAINED_MODEL_WEIGHTS = join(app.config['ROOT_DIR'], "trained_models")

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

    # if search_method == "greedy":
    #     result, _ = sampler.predict_greedy(model, np.array([evaluation_img]))
    #     print("Result greedy: {}".format(result))
    # else:
    # beam_width = int(search_method)
    print("Search with beam width: {}".format(3))
    result, _ = sampler.predict_beam_search(model, np.array([evaluation_img]), beam_width=3)
    print("Result beam: {}".format(result))

    return result


# if len(argv) < 4:
#     print("Error: not enough argument supplied:")
#     print("sample.py <trained weights path> <trained model name> <input image> <output path> <search method (default: greedy)>")
#     exit(0)
# else:
#     trained_weights_path = argv[0]
#     trained_model_name = argv[1]
#     input_path = argv[2]
#     output_path = argv[3]
#     search_method = "greedy" if len(argv) < 5 else argv[4]



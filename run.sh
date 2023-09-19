#!/bin/bash

cd datasets
zip -F pix2code_datasets.zip --out datasets.zip
unzip datasets.zip

cd ../model

./build_datasets.py ../datasets/web/all_data

./convert_imgs_to_arrays.py ../datasets/web/training_set ../datasets/web/training_features

mkdir ../bin

./train.py ../datasets/web/training_features ../bin 1

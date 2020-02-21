import os

from os.path import isfile

from utils import create_input_files

if __name__ == '__main__':
    OUTPUT_DIR = 'data/output/'

    # clear output directory
    for file in os.listdir(OUTPUT_DIR):
        if isfile(OUTPUT_DIR + file):
            os.remove(OUTPUT_DIR + file)

    # Create input files (along with word map)
    create_input_files(dataset='flickr8k',
                       karpathy_json_path='data/splits/dataset_flickr8k.json',
                       image_folder='data/img/Flicker8k_Dataset/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder=OUTPUT_DIR,
                       max_len=50)

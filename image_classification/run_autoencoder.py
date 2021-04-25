from helpers import loader
from helpers import transformer
from helpers import model
from helpers import optimizer
from helpers import metrics

import argparse
import os

class AutoEncoderClass():


if __name__ == '__main__':
    '''
        Train and test autoencoder on small set of images
    '''
    parser = argparse.ArgumentParser(description='Processing input for the model run')
    parser.add_argument('--pos_loc', dest='file_location', help='Absolute folder location of positive examples', type=str)
    parser.add_argument('--neg_loc', dest='output_location', help='Absolute folder location of negative examples', type=str)
    parser.add_argument('--config', dest='config_location', help='AutoEncoder settings', 
                        type=str, default='config/autoencoder.yaml')
    args = parser.parse_args()

    pos_example_loc = args.pos_loc
    neg_example_loc = args.neg_loc   

    # data loader


    # compile model

    # callbacks

    # model training 

    # model test

    
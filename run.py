#!/usr/bin/env python

from data import train_data_prepare
from train import train
from test import test, test_data_prepare
import os
os.environ["CUDA_VISIBLE_DEVICES"]="0"

def run(train_file, valid_file, test_file, output_file, dataset):
    '''
    Parameters
    ----------
    train_file: string
        the path to the training file
        valid_file: string
                the path to the validation file
        test_file: string
                the path to the testing file
    output_file: string
        the path to the output predictions to be saved
    '''



    #---Hyperparams
    lr = 0.001
    epoch = 1
    use_cuda = True
    num_classes = 2


    assert num_classes in [2, 6]

    #---prepare data
    train_samples, word2num = train_data_prepare(train_file, num_classes, dataset_name)
    valid_samples = test_data_prepare(valid_file, word2num, 'valid', num_classes, dataset_name)
    test_samples = test_data_prepare(test_file, word2num, 'test', num_classes, dataset_name)
    
    #---train and validate
    model = train(train_samples, valid_samples, word2num, lr, epoch, num_classes, use_cuda)
    #---test
    test(test_samples, output_file, word2num, model, num_classes, use_cuda)


dataset_name = 'LIAR-PLUS'

if dataset_name == 'LIAR':
    run('train.tsv', 'valid.tsv', 'test.tsv', 'predictions.txt', dataset_name)
else:
    run('train2.tsv', 'val2.tsv', 'test2.tsv', 'predictions.txt', dataset_name)
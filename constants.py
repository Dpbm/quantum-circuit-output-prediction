"""Constant values"""

import os

EPOCHS = 80

DEBUG = os.environ.get("DEBUG") or False

SHOTS = 1000

N_QUBITS = 5

MAX_TOTAL_GATES = 40

TOTAL_THREADS = THREADS = 10

BATCH_SIZE = 10

DATASET_SIZE = 10000
DATASET_PATH = os.path.join('.', 'dataset')
DATASET_FILE = "dataset.csv"

IMAGES_TRAIN = "images_train.h5"
IMAGES_TEST = "images_test.h5"

GHZ_FILE = "ghz.pth"
GHZ_IMAGE_FILE = "ghz.jpeg"
GHZ_PRED_FILE = "ghz-prediction.pth"

NEW_DIM = (600, 1200)


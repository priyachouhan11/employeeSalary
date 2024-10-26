# mlapp/utils.py
import pickle
import os


MODEL_PATH = os.path.join(os.path.dirname(__file__), 'lrmodel.pkl')


with open(MODEL_PATH, 'rb') as file:  # Use 'rb' for reading in binary mode
    loaded_model = pickle.load(file)

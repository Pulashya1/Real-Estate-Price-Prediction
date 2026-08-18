import pickle
import json
import numpy as np
import warnings as wrn
import os
wrn.filterwarnings('ignore')

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    if __data_columns is None or __model is None:
        return None

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    # columns: total_sqft, bath, bhk, <locations...>
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    base_dir = os.path.dirname(__file__)
    artifacts_dir = os.path.join(base_dir, 'artifacts')

    cols_path = os.path.join(artifacts_dir, 'columns.json')
    if not os.path.exists(cols_path):
        raise FileNotFoundError(f"columns.json not found at {cols_path}")

    with open(cols_path, 'r', encoding='utf-8') as f:
        __data_columns = json.load(f).get('data_columns')
        __locations = __data_columns[3:]

    model_path = os.path.join(artifacts_dir, 'banglore_home_prices_model.pickle')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"model pickle not found at {model_path}")

    if __model is None:
        with open(model_path, 'rb') as f:
            __model = pickle.load(f)

    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names()[:10])
    print(get_estimated_price('1st phase jp nagar', 1000, 3, 3))
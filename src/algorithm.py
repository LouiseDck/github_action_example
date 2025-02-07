import numpy as np

def very_complex_algorithm(param1, param2):
    param1, param2 = preprocess_params(param1, param2)
    return np.random.randint(1, 150, (param1, param2))

def preprocess_params(param1, param2):
    return param1 - 2, param2 + 2

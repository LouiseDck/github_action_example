import numpy as np

def very_complex_algorithm(param1, param2):
    param1, param2 = preprocess_params(param1, param2)
    return np.random.randint(1, 100, (param1, param2))

def preprocess_params(param1, param2):
    return param1 - 2, param2 + 2

def preprocess_params2(param1, param2):
    return param1 + 4, param2 + 4
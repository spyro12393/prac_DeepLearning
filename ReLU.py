import numpy as np

# If lesser than 0, return 0
def relu(x):
    return np.maximum(0, x)


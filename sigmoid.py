import os
# os.system("ipconfig")
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

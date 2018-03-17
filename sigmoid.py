# import os
# os.system("ipconfig")
import numpy as np
import matplotlib.pyplot as plt
# import sys
# sys.path.append("/")
import step_function

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
y2 = step_function.step_function(x)
plt.plot(x, y)
plt.plot(x, y2, linestyle = "--")
plt.ylim(-0.1, 1.1) # y limit
plt.show()
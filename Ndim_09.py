import numpy as np 

A = np.arange(10)
B = np.arange(12, dtype= int).reshape(3,4)
C = np.arange(8).reshape(2,2,2)
# ndim = number of dimesions
print(np.ndim(C))
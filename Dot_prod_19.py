import numpy as np 

A1 = np.arange(12).reshape(3,4)
A2 = np.arange(12,24).reshape(4,3)
print(np.dot(A1,A2)) # dot product of two matrix
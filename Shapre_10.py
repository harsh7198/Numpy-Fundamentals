import numpy as np 

A = np.arange(10)
B = np.arange(12, dtype= int).reshape(3,4)
C = np.arange(8).reshape(2,2,2)
# shape = tells the shape of given array
print(np.shape(A))
print(np.shape(B))
print(np.shape(C))
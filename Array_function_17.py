import numpy as np 

A1 = np.random.random((3,3))
A1 = np.round(A1 * 100)
print(A1)
print(np.max(A1)) # max return 
print(np.min(A1)) # min return 
print(np.sum(A1)) # All numbers sums 
print(np.prod(A1)) # product of All numbers
print(np.max(A1 , axis=1)) # for individual row (0 --> column , 1 --> row)
print(np.max(A1 , axis=0)) 
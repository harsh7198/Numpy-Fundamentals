import numpy as np 

A1 = np.random.random((3,3))
A1 = np.round(A1 * 100)
print(A1)
print(np.mean(A1)) # mean of whole matrix
print(np.median(A1)) # median of whole matrix
print(np.std(A1)) # std of whole matrix
print(np.var(A1)) # var of whole matrix  also used axis = 0/1
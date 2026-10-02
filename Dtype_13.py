
import numpy as np

A = np.arange(10)
B = np.arange(12, dtype=int).reshape(3, 4)
C = np.arange(8).reshape(2, 2, 2)

# dtype = return the data type of Array itmes  

print(A.dtype)
print(B.dtype)
print(C.dtype)

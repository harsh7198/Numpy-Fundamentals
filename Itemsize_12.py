
import numpy as np

A = np.arange(10)
B = np.arange(12, dtype=int).reshape(3, 4)
C = np.arange(8).reshape(2, 2, 2)

# itemsize = memory occupied by each element (in bytes)

print(A.itemsize)
print(B.itemsize)
print(C.itemsize)

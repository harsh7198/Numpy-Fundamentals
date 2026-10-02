
import numpy as np

A = np.arange(10)
B = np.arange(12, dtype=int).reshape(3, 4)
C = np.arange(8).reshape(2, 2, 2)

# astype = change the dtype of Array 

print(A.astype(np.int32)) # before its int64
print(B.astype(np.int32))
print(C.astype(np.int32))

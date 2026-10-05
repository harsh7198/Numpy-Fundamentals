import numpy as np 

A = np.arange(16).reshape(4,4)
B = np.arange(16,32).reshape(4,4)

# spliting the array 
# horizontal splitting
print(A)
print(np.hsplit(A,2)) # array name , part to cut 

# vertical splitting
print(B)
print(np.vsplit(B,2)) # array name , part to cut 
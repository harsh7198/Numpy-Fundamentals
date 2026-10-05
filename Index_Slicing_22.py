import numpy as np 

A1 = np.arange(12)
A2 = np.arange(12).reshape(3,4)
A3 = np.arange(8).reshape(2,2,2)

# used in python
# print(A1[-1]) # last index 
# print(A1[0]) 
print(A2)
print(A2[1,2]) # row number , column number to print number from 2D matrix
print(A2[2,3])

print(A3)
print(A3[1,0,1])
print(A3[0,1,0]) # in 3D matrix number , row , column 
print(A3[0,0,0]) 
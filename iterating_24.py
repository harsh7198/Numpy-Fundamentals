import numpy as np


A = np.arange(10)
B = np.arange(12, dtype= int).reshape(3,4)
C = np.arange(8).reshape(2,2,2)


for i in A:
    print(i)

for i in B:
    print(i)

for i in C:
    print(i)

for i in np.nditer(C):  # convert many dimensional array to 1D and print their numbers 
    print(i)
import numpy as np 

A = np.arange(12).reshape(3,4)
B = np.arange(12,24).reshape(3,4)
# stacking means addition or add array 
# horizontal stacking  (2 x 2) (2 x 2) = (2 x 4)
print(np.hstack((A,B)))
print("\n")
# stacking means addition or add array 
# vertical stacking  (2 x 2) (2 x 2) = (4 x 2)
print(np.vstack((A,B)))
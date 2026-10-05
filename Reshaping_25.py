import numpy as np 


# Transpose 
B = np.arange(12, dtype= int).reshape(3,4)
print(np.transpose(B))  # (3,4) ---> (4,3) 

# Ravel 
print(np.ravel(B)) # convert any Array to 1D
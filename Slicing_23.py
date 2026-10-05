import numpy as np 

A1 = np.arange(12)
A2 = np.arange(12).reshape(3,4)
A3 = np.arange(27).reshape(3,3,3)

print(A1)
print(A1[2:9])
print(A1[2:9:2]) #increment position 

print(A2)
print(A2[0,:]) # first Row , All column (:)
print(A2[:,2]) # for third column print 
print(A2[1:,1:3]) # print [5,6],[9,10]
print(A2[::2,::3]) # print 0,3,8,11  jump column and rows 
print(A2[::2,1::2]) # 1,9,3,11
print(A2[1,::3]) # print 4,7
print(A2[0:2,1:]) # print 1,2,3 5,6,7


print(A3)
print(A3[::2,:,:])
print(A3[0,1,])
print(A3[1,:,1])
print(A3[2,1:,1:])
print(A3[::2,0,0::2])
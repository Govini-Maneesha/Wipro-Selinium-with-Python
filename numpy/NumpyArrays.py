#creatong of arrays

#1d, 2d, 3D
import numpy as np
#1D
a = np.array([1,2,3])
print(a)

#2D
a = np.array([[1,2],[4,3]])
print(a)

#3D
a = np.array([[1,2],[4,3],[5,6]])
print(a)

#create array with specific data type
a = np.array([1,2,3], dtype=complex)
print(a)

a = np.array([1,2,3], dtype=float)
print(a)

a = np.array([1,2,3], dtype=int)
print(a)
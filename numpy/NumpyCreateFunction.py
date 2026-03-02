'''
    Using numpy.array() Function
    Using numpy.zeros() Function
    Using numpy.ones() Function
    Using numpy.arange() Function
    Using numpy.linspace() Function
    Using numpy.random.rand() Function
    Using numpy.empty() Function
    Using numpy.full() Function
'''


import numpy as np
#1D array
#this function creates a numpy array filled with zeros
#by default, the data  type is sloat 64

a=np.zeros(5)
print(a)

#using numpy.ones() function
a = np.ones(5)
print(a)

#2D array ones
a_2D = np.ones((4,3))
print(a_2D)

#using numpy.array() function
#the numpy.array() function creates an array by generating a sequence of numbers based on
#it is similar to python's built-in range() function

#with only the stop
a= np.arange(10)
print(a)

#providing the start, sto and step values
a= np.arange(1,10,2)
print(a)

a= np.linspace(0,10, num=6, endpoint=True)
print(a)

a= np.linspace(0,10, num=6, endpoint=False)
print(a)

a= np.random.rand(9)
print(a)

a= np.random.rand(2,3)
print(a)

a= np.random.rand(2,3,5)
print(a)

a= np.empty(2)
print(a)

a= np.empty((2,3))
print(a)

a= np.full((2,6),5)
print(a)

#numpy.eye()
#the numpy.eye() function is used to create a 2D array with ones on the diagonal and zeros in all other positions

identify_matrix = np.eye((4))
print(identify_matrix)

#numpy.identity - function is used to generate a square identity matrix.

identify_matrix = np.identity((4))
print(identify_matrix)

#numpy.diah
#in case of 2D array, the function extracts the diagonal of the array
#in the case of 1D array the function creates a square diagonal matrix with the element
#the diagonal values and zeros in remaing pisitions

Matrix=np.array([[10,20,30],[40,50,60],[70,80,90]])
print("Original matrix" ,Matrix)
Diagonal_elements=np.diag(Matrix)
print("Diagonal elements", Diagonal_elements)
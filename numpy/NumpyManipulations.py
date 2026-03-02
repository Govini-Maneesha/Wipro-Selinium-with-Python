import numpy as np

a = np.arange(1,7)
print("original array", a)
reshaped = a.reshape(2,3)
print(reshaped)

arr = np.array([[1,2],[2,3]])
for x in arr.flat:
    print(x)

#flatten - returns a copy of the array collapesd into one dimention
arr =np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.flatten()
print(at_arr)

#ravel()- returns a flattened array
arr =np.array([[1,2],[3,4]])
print(arr)
at_arr = arr.ravel()
print(at_arr)

#pad()- returns a padded array with shape increased according to pad_width
arr =np.array([1,2])
print(arr)
padded =np.pad(arr, 3,mode='constant')
print(padded)

''' Transpose operations
1   transpose
Permutes the dimensions of an array
2   ndarray.T
 as self.transpose()
3   rollaxis
Rolls the specified axis backwards
4   swapaxes
Interchanges the two axes of an array
5   moveaxis()
Move axes of an array to new positions
'''

#1  transpose
# reorders the dimensions of an array.
# rows will become the columns

arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.transpose()
print(transpose)

#2 ndarray.T
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
transpose = arr.T
print(transpose)

#rollaxis - Rolls the specified axis backwards

arr = np.zeros((2,3,4))
print(arr)

# 2 is the blocks - axis 0
# 3 - rows - axis 1
# 4 columns - axis 2

#(0,1 ,2) - (2,3,4)
#(2,0,1) - (4,2,3)

#arr[block][row][column]

new_arr = np.rollaxis(arr, 2)
print(new_arr)

#swapaxes() - Interchanges two axes of an array.
#$Axis 0 and Axis 2 swapped.
arr = np.zeros((2,3,4))
print(arr)

new_arr = np.swapaxes(arr, 0 , 2)
print(new_arr)
# (4 3, 2)

#moveaxis() - Moves specified axes to new positions.
arr = np.zeros((2,3,4))
print(arr)
new_arr = np.moveaxis(arr, 0, -1)
print(new_arr)

# (3 ,4 2)`

#joining arrays
#concatination()- joining 2 arrays
a =np.array([[1,2],[3,4]])
b =np.array([[5,6],[7,8]])
print(np.concatenate((a,b),axis=0))
print(np.concatenate((a,b),axis=1))

#srach - join thr arrays along the new axix
a =np.array([1,2,3,])
b =np.array([5,6,7])
print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))

#hstack- stacks arrays horizontaly (colum-wise)
a =np.array([[1,2],[3,4]])
b =np.array([[5,6],[7,8]])
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))
#vstack() - stacks arrays verticaly (row-wisw)
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0))

#column stack()- stack 1D array as colums into 2Darray
a =np.array([1,2,3,])
b =np.array([5,6,7])
print(np.column_stack((a,b)))
#row_stack()-stack arrays row_wise
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(np.vstack((a,b)))

#splitting arrays-converting arrays into diff subarrays based on axis
#arrsys must be divisible equally
#split
arr=np.array([1,2,3,4,5,6])
result=np.split(arr,3)
print(result)
#spli()-splits array horizantally (column-wise)
#works on 20 arrys
arr2=np.array([[1,2,3,4],
              [5,6,7,8]])
print(np.hsplit(arr2,2))

#vsplit() split arrays vertically rwo-wise
arr2=np.array([[1,2],
               [3,4],
               [5,6],
               [7,8]])
print(np.vsplit(arr2,2))
#array_split()- similar to split(), but does not require equal division
arr= np.array([1,2,3,4,5,6])
print(np.array_split(arr,3))

#adding / removing elements
#resize()- Returnins a new array with a spectified shape
arr= np.array([1,2,3,4])
new_arr = np.resize(arr, (2,3))
print(new_arr)
#the element will repeat in the new array
#returns anew array

#append() - Appends values at the end of an array
arr= np.array([1,2,3])
new_arr = np.append(arr, (4,5))
print(new_arr)

#2D array
a=np.array([[1,2],[3,4]])
b=np.array([[5,6]])
np.append(a,b, axis= 0)

#inserting values before given index,
arr = np.array([10,20,30])
new_arr= np.insert(arr,2,15)
print(new_arr)
#delete
arr = np.array([10,20,30])
new_arr= np.delete(arr,2)
print(new_arr)

#unique()
arr= np.array([1,2,2,3,3,4,5,6])
print(np.unique(arr))

#repeating
#repeat()- is used to repeat each element of an array a specified number of times.
#each element is repeates twice
arr= np.array([1,2,3])
print(np.repeat(arr,3))

#dofferent repeats for each element
arr = np.array([10,20,30])
print(np.repeat(arr,[1,2,3]))

#2Darray
arr= np.array([[1,2],
              [3,4]])
print(np.repeat(arr, 2, axis=0))

#tile()- the input array that will be repeated
arr= np.array([1,2,3,4])
tiled_array = np.tile(arr,2)
print("original array:", arr)
print("tiled array:", tiled_array)

#rearranging elements
#flip()- reverse the order of eleents along a given axis
#if axis = none then reverse entire flattended array
#if axis = 0 -> reverse row
#if axix= 1 -> reverse column

arr = np.array([1,2,3,4])
print(np.flip(arr))
#2d
arr= np.array([[1,2],
               [3,4]])
print(np.flip(arr, axis=0)) #flip rows
print(np.flip(arr, axis=1)) #flip colums
#flliplr()- Flip left right (axis=1) - works only on 2D+ arrays
arr2 = np.array([[11,2,3],
                 [3,4,7]])
print(np.fliplr(arr2))
#flipud- flip up-down (axix=0)
print(np.flipud(arr2))
#roll() - rolls (rotates) element along a given axis.
arr2= np.array([[11,2,3],
                 [3,4,7]])
print(np.roll(arr2,2,axis=None))

#sorting and searching
#sort() - returns a sorted copy of an array (or sorts in place if using ndarray method).
arr = np.array([4,8,9,5,6])
second_arr = np.sort(arr)
print(second_arr)

#argsort()- returns the indices that would sort the array returns the index positions
arr = np.array([4,8,9,5,6])
second_arr = np.sort(arr)
print(second_arr)
indices = np.argsort(arr)
print(indices)
#lexsort() - used for sorting with multiple colums(like sorting by last name, then first name
#sort by a first
#then b(secondary key)-
#sorting happens fron right -> left
a = np.array([1,0,1,0])
b = np.array([1,1,0,0])
result= np.lexsort((b,a))
print(result)

print(np.zeros((2,2)) )
a = np.array([1,2,3])
print(a*2 )
print(np.linspace(0,10,5) )
print(np.full((2,2),5) )
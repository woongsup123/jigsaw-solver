import numpy as np
import helper
'''
arr1 = [0, 1, 2]
arr2 = [3, 4, 5]
arr3 = [6, 7, 8]

arr = [arr1, arr2, arr3]

width = len(arr)
height = len(arr[0])
print(width)
print(height)

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2 = np.array([[4, 3, 6], [2, 5, 2]])


print(arr1)
print(arr2)
print(np.append(arr1, arr2, axis=0))
'''

arr = [[1, 2, 4, 1, 5], [6, 0, 0, 0, 2], [0, 0, 0, 1, 0] , [9, 3, 0, 1, 0] , [8, 7, 2, 1, 3]]
width, height = arr.size
np_piece = np.array(arr, dtype='int64')
    # define each piece as a Piece object2
    # Piece object consists of four edges
edge1 = np_piece[0,:]
edge2 = np_piece[:,height-1]
edge3 = np_piece[width-1,:]
edge4 = np_piece[:,0]
long_edge1 = np_piece[:,]

edges = [edge1, edge2, edge3[::-1], edge4[::-1]]
print("==============")
print(edges[0])
print("==============")
print(edges[0])
print("==============")
print(edges[0])
print("==============")
print(edges[0])
# add each piece object into the array

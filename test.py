import numpy as np

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

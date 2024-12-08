import numpy as np

def arr(row, col):
    arr_ = np.random.rand(row, col)
    return arr_
arr1 = arr(5, 3)
print(arr1)
print()

def em(row, col, value):
    arr_1 = np.full((row, col), value)
    return arr_1
arr2 = em(2, 8, 5)
print(arr2)
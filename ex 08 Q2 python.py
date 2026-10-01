import numpy as np

a = np.array([10, 20, 30], dtype=int)
b = np.array([1.5, 2.5, 3.5], dtype=float)
c = np.array([True, False, True], dtype=bool)

print("Integer array:", a)
print("Data type:", a.dtype)

print("Float array:", b)
print("Data type:", b.dtype)

print("Boolean array:", c)
print("Data type:", c.dtype)



arr1 = np.array([1, 2, 3, 4])
print("\n1-D Array:", arr1)


arr2 = np.array([[1, 2], [3, 4]])
print("2-D Array:")
print(arr2)


arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])
print("3-D Array:")
print(arr3)

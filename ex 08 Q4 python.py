import numpy as np
# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Sum:", np.sum(arr))

print("\nBroadcasting Examples:")

print("Array + 5:", arr + 5)

print("Array * 2:", arr * 2)

arr2 = np.array([1, 2, 3, 4, 5])
print("Array + [1,2,3,4,5]:", arr + arr2)

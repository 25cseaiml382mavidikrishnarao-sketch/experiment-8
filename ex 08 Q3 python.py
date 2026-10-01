import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])
print("Array:")
print(arr)

print("\n--- Array Properties ---")
print("Number of dimensions (ndim):", arr.ndim)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)
print("Item size:", arr.itemsize)

print("\n--- NumPy Functions ---")
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))
print("Transpose:")
print(np.transpose(arr))

print("\nReshaped array:")
print(arr.reshape(3, 2))

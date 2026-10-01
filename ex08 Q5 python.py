import numpy as np


arr = np.array([10, 20, 30, 40, 50])


np.save("myarray.npy", arr)

print("Array saved successfully.")


loaded_arr = np.load("myarray.npy")

print("Loaded Array:")
print(loaded_arr)

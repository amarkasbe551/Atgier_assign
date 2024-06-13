import numpy as np

# Array 'ones' from Question-5
ones = np.ones((2, 5), dtype=int)

# Reshape the array to have all 10 elements in a single row
ones_reshaped = ones.reshape(1, -1)

# Print the reshaped array
print("Reshaped array 'ones':")
print(ones_reshaped)

import numpy as np

# Arrays from Question-5
zeros = np.zeros(10)
vowels = np.array(['a', 'e', 'i', 'o', 'u'])
ones = np.ones((2, 5), dtype=int)
data = [
    [2.7, -2, -19],
    [0, 3.4, 99.9],
    [10.6, 0, 13]
]
myarray1 = np.array(data)
myarray2 = np.arange(4, 4*3*5+4, 4, dtype=float).reshape(3, 5)

# Display dimensions, shape, size, data type, and itemsize of arrays
print("Array 'zeros':")
print("  Dimensions:", zeros.ndim)
print("  Shape:", zeros.shape)
print("  Size:", zeros.size)
print("  Data type:", zeros.dtype)
print("  Itemsize:", zeros.itemsize)

print("\nArray 'vowels':")
print("  Dimensions:", vowels.ndim)
print("  Shape:", vowels.shape)
print("  Size:", vowels.size)
print("  Data type:", vowels.dtype)
print("  Itemsize:", vowels.itemsize)

print("\nArray 'ones':")
print("  Dimensions:", ones.ndim)
print("  Shape:", ones.shape)
print("  Size:", ones.size)
print("  Data type:", ones.dtype)
print("  Itemsize:", ones.itemsize)

print("\nArray 'myarray1':")
print("  Dimensions:", myarray1.ndim)
print("  Shape:", myarray1.shape)
print("  Size:", myarray1.size)
print("  Data type:", myarray1.dtype)
print("  Itemsize:", myarray1.itemsize)

print("\nArray 'myarray2':")
print("  Dimensions:", myarray2.ndim)
print("  Shape:", myarray2.shape)
print("  Size:", myarray2.size)
print("  Data type:", myarray2.dtype)
print("  Itemsize:", myarray2.itemsize)

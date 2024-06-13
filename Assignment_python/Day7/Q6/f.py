import numpy as np

data = [
    [2.7, -2, -19],
    [0, 3.4, 99.9],
    [10.6, 0, 13]
]
myarray1 = np.array(data)

print("Elements in the 1st column of 'myarray1':", myarray1[:, 0])
print("Elements in the 2nd column of 'myarray1':", myarray1[:, 1])

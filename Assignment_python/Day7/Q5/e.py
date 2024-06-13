# e) A 2-D array called myarray2 using arange() having 3 rows and 5 columns with start value = 4, step size 4 and dtype as float.

import numpy as np

# Create myarray2 using arange with start value 4, step size 4, 3 rows, 5 columns, and dtype float
myarray2 = np.arange(4, 4*3*5+4, 4, dtype=float).reshape(3, 5)

print("Array 'myarray2':")
print(myarray2)

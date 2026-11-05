# NumPy, which stands for Numerical Python, is the foundational open-source Python library used for scientific computing, data analysis, and machine learning
# @ operator is for multiplication between metrics

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Using *:")
print(A * B)

print("Using @:")
print(A @ B)



# Feature	                    Python List	                        NumPy Array
# Creation	                [1, 2, 3]	                        np.array([1, 2, 3])
# Data types	                Can mix types easily            	Usually uses one common data type
# Mathematical operations	    Often need loops	                Can operate on all elements directly
# Matrix operations	        Not built in directly	            Supports operations like @
# Best for	                General-purpose data storage	    Numerical calculations and scientific computing

list = [1,2,3]
print(list * 2)

array = np.array([1,2,3])
print(array*2)
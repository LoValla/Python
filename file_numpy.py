# NUMPY (Numerical Python) gives access to a broad range of instruments for scientific computing
# The core of the numpy library are numpy ARRAYS, that behave differently wrt lists

import numpy as np

x = np.array([1, 2, 3, 4])  # access ith element with x[i]
y = np.array([3, 4, 5, 6])

print(f"numpy arrays, x + y = {x+y}")
print(f"numpy arrays, x * 3 = {x*3}")

print(x[slice(3)])  # the elements up to x[3]
print(x[slice(1, 3)])  # the elements x[1] and x[2]
print(x[slice(0, 3, 2)])  # the elements x[0] and x[2] (2 is the slicing STEP)
print(x[[0, 2]])  # this does not work for lists, but only arrays

points = np.array([[0, 1, 2], [3, 4, 5]])

print(
    "array type = {}".format(points.dtype)
)  # an array can only have one data type (e.g. not mixed int and float)
print("array shape = {}".format(points.shape))  # number of elements along each axis
print("array size = {}".format(points.size))  # total number of elements
print("number of array axes = {}".format(points.ndim))  # number of axes (dimensions)

"""
Three key features of Numpy:
1) Vectorization - Computations without explicit 'for' loops (that are very slow in python)
2) Broadcasting - Implicit operations between arrays with different sizes
3) Sub-arrays operations (Slicing, Indexing, Masks) 
"""

a = np.random.randint(low=1, high=100, size=10000)

def explicit_loop_for_inverse(array):
    res = []
    for a in array:
        res.append(1./a)
        return np.array(res)
    
b = explicit_loop_for_inverse(a) # very slow (explicit for)
b = [1./x for x in a] #slow (list comprehension)
b = 1./a #FAST - VECTORIZATION

#in the same way, we can use vectorization with many functions such as np.exp(a), np.cos(a), a**3, ...

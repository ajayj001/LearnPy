import numpy as np
np.random.seed(0)  # seed for reproducibility

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

print("x3 ndim: ", x3.ndim)
print("x3 shape:", x3.shape)
print("x3 size: ", x3.size)

print("dtype:", x3.dtype)

print("itemsize:", x3.itemsize, "bytes") #itemsize, which lists the size (in bytes) of each array element, 
print("nbytes:", x3.nbytes, "bytes")#nbytes, which lists the total size (in bytes) of the array:

x = np.arange(10) # to genrate an arrayof 10
print("use of arange:",x)
print("use of slicing: ",x1[1:5:2]) #x[start:stop:step]


x[:5]  # first five elements
x[5:]  # elements after index 5
x[4:7]  # middle sub-array
x[::2]  # every other element
x[1::2]  # every other element, starting at index 1
x[::-1]  # all elements, reversed
x[5::-2]  # reversed every other from index 5

print("X2 is: ", x2)
x2[:2, :3]  # two rows, three columns
x2[:3, ::2]  # all rows, every other column
x2[::-1, ::-1]
print(x2[0])  # equivalent to x2[0, :]

# To copy the array and not use views
x2_sub_copy = x2[:2, :2].copy()
print("copy:", x2_sub_copy)


# Another useful type of operation is reshaping of arrays. reshape method

grid = np.arange(1, 10).reshape((3, 3))
print("Grid",grid)


x = np.array([1, 2, 3])

# row vector via reshape
x.reshape((1, 3))
print("X after reshape: ", x)
# row vector via newaxis
x[np.newaxis, :]
print("X after newaxis: ", x)
 

import numpy as np

## Fancy indeing
rand = np.random.RandomState(42)

x = rand.randint(100, size=10)
print(x)
print(x[x>50])
print([x[3], x[7], x[2]])
ind = [3, 7, 4]
print(x[ind])
row = np.array([0, 1, 2])
col = np.array([2, 1, 3])
X = np.arange(12).reshape((3, 4))
X[row, col]
print(X[row[:, np.newaxis], col])
print( row[:, np.newaxis] *col)
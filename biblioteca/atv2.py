import numpy as np

matriz1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matriz2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

mres = [[0,0,0]],[[0,0,0]],[[0,0,0]]

mres = matriz1 - matriz2

print(matriz1)
print()
print(matriz2)
print()
print(mres)

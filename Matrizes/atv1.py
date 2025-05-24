matriz_a = [
    [1, 2],
    [4, 5]
]

for i in range(2):
    for j in range(2):
        print(f'{i} {j} {matriz_a[i][j]}')
matriz_b = [
    [5, 6],
    [7, 8]
]

for i in range(2):
    for j in range(2):
        print(f'{i} {j} {matriz_b[i][j]}')

matriz_c = matriz_a + matriz_b
print(matriz_c)
import random

matriz1 = []
matriz2 = []

for i in range(10):
    linha1 = []
    linha2 = []
    for j in range(10):
        linha1.append(random.randint(0, 9))
        linha2.append(random.randint(0, 9))
    matriz1.append(linha1)
    matriz2.append(linha2)

for i in range(10):
    for j in range(10):
        if matriz1[i][j] == matriz2[i][j]:
            print(f"Valor igual: {matriz1[i][j]}  na posição: {i}, {j}")

print("\nMatriz 1:")
for linha in matriz1:
    print(linha)

print("\nMatriz 2:")
for linha in matriz2:
    print(linha)

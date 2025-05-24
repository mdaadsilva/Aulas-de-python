# Faça um programa que leia uma matriz 4x4. Depois conte e escreva quantos valores maiores que 10 ela possui.

matriz = []
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
print("Matriz 4x4:")
for linha in matriz:
    print(linha)
maior_que_dez = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            maior_que_dez += 1
print(f"Quantidade de valores maiores que 10: {maior_que_dez}")

#faça um programa que leia uma matriz 3x3. Calcule e mostre a soma dos elementos da diagonal principal.
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)
print("Matriz 3x3:")
for linha in matriz:
    print(linha)
soma_diagonal = 0
for i in range(3):
    soma_diagonal += matriz[i][i]
print(f"Soma dos elementos da diagonal principal: {soma_diagonal}")
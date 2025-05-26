#crie uma lista 3x3 e preencha com valores inteiros, depois verifique se o valor 5 está presente na lista e imprima a posição se estiver presente, caso contrário, imprima que não foi encontrado.

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
x = 5
encontrado = False
for i in range(3):
    for j in range(3):
        if matriz[i][j] == x:   
            print(f"Valor {x} encontrado na posição [{i}][{j}]")
            encontrado = True
if not encontrado:
    print(f"Valor {x} não encontrado na matriz.")
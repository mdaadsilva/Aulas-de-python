#Faça um programa que leia uma matriz 3x3. Leia tambem um valor X inserido pelo usuario. O programa deve fazer a busca desse valor na matriz e mostrar caso encontre o valor, a posição em que ele se encontra. Caso não encontrar, mostrar "não encontrado na posição [i][j]".

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
x = int(input("Digite o valor a ser buscado na matriz: "))
encontrado = False
for i in range(3):
    for j in range(3):
        if matriz[i][j] == x:   
            print(f"Valor {x} encontrado na posição [{i}][{j}]")
            encontrado = True
if not encontrado:
    print(f"Valor {x} não encontrado na matriz.")

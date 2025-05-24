#Ler uma matriz 2x3, solicitando os valores ao usuário, Mostrar a matriz completa no final

matriz = []
for i in range(2):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)
print('A matriz é:')
for i in matriz:
    print(i)
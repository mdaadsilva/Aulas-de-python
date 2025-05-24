#Crie uma matriz 3x3 com valores inseridos pelo usuario e exiba a matriz no formato de tabela

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para a posição [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)
print('A matriz é:')
for i in matriz:
    print(i)
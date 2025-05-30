matriz = []

print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento a{i+1}{j+1}: "))
        linha.append(valor)
    matriz.append(linha)

diagPrin = (
    matriz[0][0] * matriz[1][1] * matriz[2][2] +
    matriz[0][1] * matriz[1][2] * matriz[2][0] +
    matriz[0][2] * matriz[1][0] * matriz[2][1]
)

diagSec = (
    matriz[0][2] * matriz[1][1] * matriz[2][0] +
    matriz[0][0] * matriz[1][2] * matriz[2][1] +
    matriz[0][1] * matriz[1][0] * matriz[2][2]
)

det = diagPrin - diagSec

print("\nMatriz 3x3:")
for linha in matriz:
    print(linha)

print(f"\nDeterminante: {det}")

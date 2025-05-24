# Faça um programa em Python para leia um vetor de 10 posições. Contar e
# escrever quantos valores pares ele possui e as posições (índices) em que se
# encontram.

Vetor = []
for i in range(10):
    num = int(input("Digite um número: "))
    Vetor.append(num)
print("Valores pares e suas posições:")
contagem = 0
for i in range(len(Vetor)):
    if Vetor[i] % 2 == 0:
        print(f"Valor: {Vetor[i]}, Posição: {i}")
        contagem += 1
print(f"Total de valores pares: {contagem}")

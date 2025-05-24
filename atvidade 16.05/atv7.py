# Escreva um programa Python para mover todos os valores zero para o final do
# vetor, ou seja, para a direita, sem alterar a ordem dos elementos diferentes de zero já
# presentes na lista e sem criar um vetor adicional ou temporário.

Vetor = []
for i in range(10):
    num = int(input("Digite um número: "))
    Vetor.append(num)
print("Lista original:", Vetor)

n = len(Vetor)
pos = 0
for i in range(n):
    if Vetor[i] != 0:
        Vetor[pos], Vetor[i] = Vetor[i], Vetor[pos]
        pos += 1
print("Lista após mover zeros para o final:", Vetor)
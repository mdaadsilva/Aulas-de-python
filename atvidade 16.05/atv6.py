# Faça um programa em Python que leia um vetor de 10 posições. Em seguida
# percorra essa lista verificando se existem itens de valores iguais, caso iguais
# escreva os na tela.

Vetor = []
for i in range(10):
    num = int(input("Digite um número: "))
    Vetor.append(num)
print("Valores iguais e suas posições:")
valores_iguais = set()
for i in range(len(Vetor)):
    for j in range(i + 1, len(Vetor)):
        if Vetor[i] == Vetor[j]:
            valores_iguais.add(Vetor[i])
            print(f"Valor: {Vetor[i]}, Posições: {i}, {j}")
if len(valores_iguais) == 0:
    print("Não existem valores iguais na lista.")
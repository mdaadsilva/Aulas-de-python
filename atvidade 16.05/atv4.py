#  Faça um programa para ler uma lista de 10 números reais e mostre-os na ordem
# inversa.
Lista = []
for i in range(10):
    num = float(input("Digite um número real: "))
    Lista.append(num)
print("Lista de números na ordem inversa:")
for i in range(len(Lista)-1, -1, -1):
    print(Lista[i])
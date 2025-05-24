# Escreva um código para ler uma lista de 5 números inteiros e mostrar cada
# número juntamente com a sua posição na lista.

Lista = []
for i in range(5):
    num = int(input("Digite um número inteiro: "))
    Lista.append(num)
print("Lista de números e suas posições:")
for i in range(len(Lista)):
    print(f"Número: {Lista[i]}, Posição: {i}")

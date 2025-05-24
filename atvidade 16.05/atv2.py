# Desenvolva um algoritmo que solicite o nome de uma pessoa e armazene em
# uma lista enquanto o nome da pessoa seja diferente de "sair". Após sair, exiba a lista
# de todos dos nomes.

Lista = []
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para sair): ")
    if nome.lower() == "sair":
        break
    Lista.append(nome)
print("Lista de nomes:")
for item in Lista:
    print(item)
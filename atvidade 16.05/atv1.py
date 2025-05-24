#Faça uma lista de compras solicitando cada produto e adicionando em uma lista
#utilize "x" para sair da repetição. Ao final exiba a lista de compras
Lista = []
while True:
    produto = input("Digite o produto que deseja adicionar a lista de compras (ou 'x' para sair): ")
    if produto.lower() == "x":
        break
    Lista.append(produto)
print("Lista de compras:")
for item in Lista:
    print(item)
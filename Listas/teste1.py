# Faça um programa ue leia N nomes. Ao digitar "sair" interromper a leitura de dados. Ao final, mostrar os nomes obtidos#

lerNomes = []
print("Digite os nomes (digite 'sair' para parar): ")
while True:
    nome = input("Nome: ")
    if nome.lower() == "sair":
        break
    lerNomes.append(nome)
print("Nomes obtidos: ", lerNomes)
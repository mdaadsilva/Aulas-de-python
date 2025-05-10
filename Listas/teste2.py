# Faça um outro programa que leia N nomes de animais. Mostre as alterações inseridas ao usuário e permita que ele possa alterar qualquer um dos nomes. Ao final, mostre os nomes obtidos #

LerAnimais = []
print("Digite o nome de animais")
for i in range(5):
    LerAnimais.append(input(f"Digite o nome do {i+1}º animal: "))
print("Os animais digitados foram:")
for i in range(5):
    print(f"{i+1}º animal: {LerAnimais[i]}")

while True:
    print("\nCaso queira alterar algum nome, digite o número do animal que deseja alterar:")
    for i in range(5):
        print(f"{i+1}º animal: {LerAnimais[i]}")
    alterarNome = input("Digite o número do animal que deseja alterar (ou 'sair' para encerrar): ")

    if alterarNome.lower() == 'sair':
        break

    if not alterarNome.isdigit():
        print("Entrada inválida: digite um número válido.")
    else:
        alterarNome = int(alterarNome)
        if alterarNome < 1 or alterarNome > 5:
            print("Número inválido: escolha um número entre 1 e 5.")
        else:
            LerAnimais[alterarNome-1] = input(f"Digite o novo nome do {alterarNome}º animal: ")

print("\nOs animais atualizados são:")
for i in range(5):
    print(f"{i+1}º animal: {LerAnimais[i]}")

print("\nObrigado por usar o programa!")

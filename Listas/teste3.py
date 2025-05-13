#Faça um programa que leia N numeros. mostre a lista completa removendo o ultimo item da lista#

lerNumeros = []
print("Digite os números (digite 'sair' para parar): ")
while True:
    numero = input("Número: ")
    if numero.lower() == "sair":
        break
    lerNumeros.append(numero)
print("Números obtidos: ", lerNumeros)
lerNumeros.pop()
print("Lista após remover o último item: ", lerNumeros)
print("Obrigado por usar o programa!")
#Faça um programa que leia N numeros e mostre a lista completa depois mostre a lista removendo o primeiro item da lista

lerNumeros = []
print("Digite os números (digite 'sair' para parar): ")
while True:
    numero = input("Número: ")
    if numero.lower() == "sair":
        break
    lerNumeros.append(numero)
print("Números obtidos: ", lerNumeros)
lerNumeros.pop(0)
print("Lista após remover o primeiro item: ", lerNumeros)
print("Obrigado por usar o programa!")

#Faça um programa que leia N numeros. Mostre a lista completa, depois remova o primeiro item da lista e mostre a lista novamente.#
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

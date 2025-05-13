#Faça um programa que leia N numeros. mostre a lista completa, depois mostre o maior numero da lista.#
lerNumeros = []
print("Digite os números (digite 'sair' para parar): ")
while True:
    numero = input("Número: ")
    if numero.lower() == "sair":
        break
    lerNumeros.append(numero)
print("Números obtidos: ", lerNumeros)
if len(lerNumeros) > 0:
    maiorNumero = max(lerNumeros)
    print("O maior número da lista é: ", maiorNumero)
else:
    print("Nenhum número foi digitado.")
print("Obrigado por usar o programa!")

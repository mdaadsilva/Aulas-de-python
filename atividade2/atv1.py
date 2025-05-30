numeros = []

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

referencia = int(input("Digite o valor de referência inteiro: "))

contador = 0
for numero in numeros:
    if numero < referencia and numero % 2 != 0:
        contador += 1

print("Quantidade de números menores que o valor de referência e ímpares:", contador)

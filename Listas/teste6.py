#Faça um programa que leia N numeros mostre  lista comppleta e depois mostre o maior numero e menor numero da lista

LerNumeros = []
print("Digite os números (digite 'sair' para parar): ")
while True:
    numero = input("Número: ")
    if numero.lower() == "sair":
        break
    if not numero.isdigit():
        print("Entrada inválida: digite um número válido.")
        continue
    LerNumeros.append(int(numero))
print("Números obtidos: ", LerNumeros)
if LerNumeros:
    maiorNumero = max(LerNumeros)
    menorNumero = min(LerNumeros)
    print(f"O maior número é: {maiorNumero}")
    print(f"O menor número é: {menorNumero}")
else:
    print("Nenhum número foi digitado.")
print("\nObrigado por usar o programa!")

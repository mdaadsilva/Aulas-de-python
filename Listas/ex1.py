lista1 = []
print("Digite os elementos da primeira lista (0 para parar): ")
while True:
    n=int(input("Nº: "))
    if n==0:
        break
    lista1.append(n)

####################################################################    

lista2 = []
print("Digite os elementos da segunda lista (0 para parar): ")
while True:
    n=int(input("Nº: "))
    if n==0:
        break
    lista2.append(n)

####################################################################

lista3 = []
for item in lista1 + lista2:
    if item not in lista3:
        lista3.append(item)
print("Terceira lista sem elemntos repetidos: ", lista3)

####################################################################

lista = ['a', 'b', 'c', 'd', 'e']
del (lista[1])
print(lista)

####################################################################

lista = list(range(101))
print(lista)

del lista[40:61]
print(lista)



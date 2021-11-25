from itertools import permutations

ilosc = int(input("ilosc elementow: "))
lista = []
for i in range(0,ilosc):
    if i == 0:
        x = int(input('Podaj pierwszy:'))
    else:
        x = int(input('Podaj kolejny:'))
    lista.append(x)

for x in permutations(lista):
    print (x)
from itertools import permutations

ilosc = int(input("ilosc elementow "))
lista = []
for i in range(0,ilosc):
    x = int(input())
    lista.append(x)

for x in permutations(lista):
    print (x)
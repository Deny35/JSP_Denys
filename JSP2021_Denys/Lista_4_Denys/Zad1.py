ilosc = int(input('Podaj ilość liczb: '))
liczby = []
suma = 0
iloczyn = 1
for i in range(0,ilosc):
    x = int(input())
    liczby.append(x)
   # suma = suma + liczby[i]
   # iloczyn = iloczyn * liczby[i]
print(liczby)

#print('Suma: ', suma)
#print('Iloczyn: ', iloczyn)

import math

print("Suma: ", sum(liczby))
print("Iloczyn: ", math.prod(liczby))

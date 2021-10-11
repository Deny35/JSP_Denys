#zad.1
a = input()
b = input()
suma = a +b
print(suma)
#Input domyślnie zapisuje jako string i zamista dodac int to dodał ciąg znaków.

#zad.2
import math

def pole(a, b, alfa):
    if(a <= 0 or b <= 0 or alfa <=0):
        return1
    else:
     return 0.5*a*b*math.sin(math.radians(alfa))

print(pole(3, 4, 47))

#zad.3

a= int(input('Bok a:'))
b = int(input('Bok b:'))
alfa = int(input('Kąt alfa:'))
print(pole(a, b, alfa))

#zad.4
import builtins
dir(builtins)
help(print)
print('Ala ma kota')
print(2+2 \t)
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
        return
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
print("Ala ma kota")
print(2+2)
print(2*5, "\t", 35//2, "\t", 35/2, "\t", 35 % 2)
print("", 2*5, "\n", 35//2, "\n", 35/2, "\n", 35 % 2)



#zad.5
print(7//3)
print(round(7/3))
print(math.floor(7/3))
# Różnica jest taka, że round zaokrągla do 0.5 w dół, a od 0.5 w górę, floor zaokrągla tylko w dół, a  // podaje tylko liczbę całkowitą liczbe z dzielenia

#zad.6
import math

x = complex((-17)**0.5)
print(x)

#zad.7


#zad.8
print('Napisz liczbe a i b,aby a>b')
a = float(input('Liczba a:'))
b = float(input('Liczba b:'))
Z = b/a
Z += 3
print(Z)

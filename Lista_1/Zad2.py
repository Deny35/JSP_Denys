#zad.2
import math

def pole(a, b, alfa):
    if(a <= 0 or b <= 0 or alfa <=0):
        return1
    else:
     return 0.5*a*b*math.sin(math.radians(alfa))

print(pole(3, 4, 47))
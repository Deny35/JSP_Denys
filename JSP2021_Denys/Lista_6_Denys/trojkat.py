import math

def obwod(a, b, c):
    return a+b+c

def pole (a, b, c):
    pole = math.sqrt(((1 / 2) * obwod(a, b, c)) 
    * (((1 / 2) * obwod(a, b, c)) - a)
    * (((1 / 2) * obwod(a, b, c)) - b) 
    * (((1 / 2) * obwod(a, b, c)) - c))
    return round(pole, 2)

def rodzaj_bokow(a, b, c):
    if a == b and b == c:
        return 'trójkąt równoboczny'
    elif a == b or a == c or b == c:
        return 'trójkąt równoramienny'
    else:
        return 'trójkąt różnoboczny'

def rodzaj_konta(a , b, c):
    if a >= b and a >= c:
        if a ** 2 > b ** 2 + c ** 2:
            return 'rozwartokątny'
        elif a ** 2 == b ** 2 + c ** 2:
            return 'prostokątny'
        else:
            return 'ostrokątny'
    elif b >= a and b >= c:
        if b ** 2 > a ** 2 + c ** 2:
            return 'rozwartokątny'
        elif b ** 2 == a ** 2 + c ** 2:
            return 'prostokątny'
        else:
            return 'ostrokątny'
    elif c >= a and c >= b:
        if c ** 2 > a ** 2 + b ** 2:
            kat = 'rozwartokątny'
        elif c ** 2 == a ** 2 + b ** 2:
            return 'prostokątny'
        else:
            return 'ostrokątny'

    

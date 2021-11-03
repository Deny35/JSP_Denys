klucz ={'a':'y', 'e':'i', 'i':'o', 'o':'a', 'y':'e'}
klucz1 = {v: k for k, v in klucz.items()}
print(klucz)
print(klucz1)

def szyfrowanie(zdanie):
    zdanie = list(zdanie) #zmienia w liste
    for i in range(0, len(zdanie)):
        if zdanie[i] in klucz:
            zdanie[i] = (klucz.get(zdanie[i]))# zmienia litery
    x =''
    zdanie = x.join(zdanie)# spaja litery
    return zdanie

def deszyfrowanie(zdanie):
    zdanie = list(zdanie)
    for i in range(0, len(zdanie)):
        if zdanie[i] in klucz1:
            zdanie[i] = (klucz1.get(zdanie[i]))
    x =''
    zdanie = x.join(zdanie)
    return zdanie

zdanie = input('Podaj zdanie: ')
szyfr = szyfrowanie(zdanie)
dszyfr = deszyfrowanie(szyfr)
print('Zaszyfrowane: ', szyfr)
print('Deszyfrowany: ', dszyfr)

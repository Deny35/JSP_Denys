import trojkat

a = int(input('Podaj bok a: '))
b = int(input('Podaj bok b: '))
c = int(input('Podaj bok c: '))

print('Obwód=',trojkat.obwod(a, b, c))
print('Pole=',trojkat.pole(a, b, c))
print(trojkat.rodzaj_bokow(a, b, c))
print(trojkat.rodzaj_konta(a, b, c))
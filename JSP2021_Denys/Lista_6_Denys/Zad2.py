import SzyfrCezara

tekst = input('Podaj zdanie:')
klucz = int(input('Podaj klucz syfrowania:'))
szyfr = SzyfrCezara.szyfrowanie(tekst, klucz)
print('Zaszyfrowane:',szyfr)
dszyfr = SzyfrCezara.deszyfrowanie(szyfr , klucz)
print('Deszyfrowane:',dszyfr)
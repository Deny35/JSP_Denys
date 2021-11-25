ilosc = int(input('Podaj ilość liczb: '))
liczby = []
for i in range(0,ilosc):
    if i == 0:
        x = int(input('Podaj pierwszy: '))
    else:
        x = int(input('Podaj kolejny:'))
    liczby.append(x)
liczby_bez = list(set(liczby))# funkcja set tworzy kolejke z unikalnymi elementami
                              #, a list zamienia kolekcje na liste
print(liczby_bez)

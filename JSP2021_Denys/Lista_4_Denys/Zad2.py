ilosc = int(input('Podaj ilość liczb: '))
liczby = []
for i in range(0,ilosc):
    x = int(input())
    liczby.append(x)
liczby_bez = list(set(liczby))# funkcja set tworzy kolejke uporządkowaną z unikalnymi elementami
                              #, a list zamienia kolekcje na liste
print(liczby_bez)

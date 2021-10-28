tlumacz={'zero': 0,'jeden': 1, 'dwa':2,'trzy' :3, 'cztery': 4, 'pięć': 5, 'sześć': 6, 'siedem' : 7, 'osiem' : 8,
         'dziewięć':9, 'dziesięć': 10, 'jedenaście': 11,'dwanaście': 12, 'trzynaście': 13, 'czternaście':14, 'piętnaście': 15,
         'szesnaście':16, 'siedemnaście':17, 'osiemnaście':18, 'dziewiętnaście':19,'dwadzieścia':20,
          'trzydzieści':30, 'czterdzieści':40, 'pięćdziesiąt':50}#Przypożudkuje słową ich odpowednich w liczbach. Przed dwukropkie
                                                                 # jesy keyname, a po wartość jej przypisana

def zamiana(dzi,jed):
    j = 0
    p = 0
    if(dzi in tlumacz):
        k=(tlumacz.get(dzi))#zmienia na liczbe
    if(jed in tlumacz):
        j=(tlumacz.get(jed))#zmienia na liczbe
    print(k+j)


x= input('Podaj słownie liczbę: ')
y=x.split()
print(y)
zamiana(y[0],y[1])
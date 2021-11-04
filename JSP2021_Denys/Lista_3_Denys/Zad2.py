liczba = int(input ('Wprowadz liczbe całkowitą:'))
if(liczba%2==0):
    print('Liczba jest liczbą parzystą')
else:
    print('Liczba jest liczbą nieparzystą')
################################################################
print('##############################')
odp = ('Parzysta', 'Nieparzysta')
print ('bez if:',odp[liczba%2])
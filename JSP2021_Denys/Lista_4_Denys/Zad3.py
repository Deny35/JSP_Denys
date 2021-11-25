def zamina(wybor, x):
    import math
    if (wybor=='R' or wybor=='r'):
        return ('To '+ str(math.radians(x)) +' radianów')
    elif (wybor=='S' or wybor=='s'):
        return ('TO ' + str(math.degrees(x)) + ' stopni') 

print('Chcesz zamienć na radioany na stopnie czy stopnie na radiany?')
print('Jeżeli radioany na stopnie wpisz "S", a jeżeli stopnie na radiany wpisz "R".')
wybor = input('Wybór: ')
if (wybor=='R' or wybor=='r'):
    x = float(input('Podaj stopień: '))
elif (wybor=='S' or wybor=='s'):
    x = float(input('Podaj radian: '))
print(zamina(wybor, x))





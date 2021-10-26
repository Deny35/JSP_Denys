import math
a = int(input('Podaj a:'))
b = int(input('Podaj b:'))
c = int(input('Podaj c:'))

if(a == 0):
    print('Równanie nie jest rówaniem kwadratowym.')
else:
    delta = b**2-(4*a*c)

if(delta == 0):
    x0 = -b/(2*a)
    print('x0:')
elif(delta > 0):
      x1 = ((-b) - math.sqrt(delta))/(2 * a)
      x2 = ((-b) + math.sqrt(delta))/(2 * a)
      print ('x1=',x1,'    x2=', x2)
else:
    print('Brak rozwiązań.')

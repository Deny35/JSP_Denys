import math
import cmath

x = float(input("Podaj część rzeczywistą "))
y = float(input("Podaj część urojoną"))
z = complex(x, y) # Zamienia na zwspoloną
print('Moduł:', math.sqrt(x**2 + y**2)) # Zwraca moduł
print('Argument:', cmath.phase(z)) #Zwraca argument

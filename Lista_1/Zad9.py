import math
import cmath

x = float(input("Podaj część rzeczywistą "))
y = float(input("Podaj część urojoną"))
z = complex(x, y)
print('Moduł:', math.sqrt(x**2 + y**2))
print('Argument:', cmath.phase(z))

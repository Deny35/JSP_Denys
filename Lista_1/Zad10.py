import cmath

x = 0
y = 1

z = complex(x, y)

print("rzeczywiste")
print(cmath.sin(z).real)
print(cmath.cos(z).real)

print("urojone")
print(cmath.sin(z).imag)
print(cmath.cos(z).imag)

a = cmath.sin(z) ** 2 + cmath.cos(z) ** 2
print(a)
if (a==1):
    print('Tak, założenie sin^2(z)+cos^2(z)=1 jest spaełnione.')
else:
    print('Nie jest spełnione.')


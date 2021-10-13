import cmath

x = 0
y = 1

z = complex(x, y)

print('Część rzeczywista:')
print('sin:   ', cmath.sin(z).real)
print('cos:   ', cmath.cos(z).real)

print('Część urojona:')
print('sin:   ', cmath.sin(z).imag)
print('cos:   ', cmath.cos(z).imag)

a = cmath.sin(z) ** 2 + cmath.cos(z) ** 2
print('Tak, założenie sin^2(z)+cos^2(z)=', a, 'jest spaełnione.')


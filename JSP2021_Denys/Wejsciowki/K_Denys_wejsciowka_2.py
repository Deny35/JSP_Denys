import math
def wielomian(x,a):
    f = 0
    for i in range (0,len(a)):
        if i == 0:
            f += a[i]
        else:
            iks = math.pow(x,i)
            w = a[i]*iks
            f += w
    return f

a = [1, 2, 4]
x = 5
print(wielomian(x,a))
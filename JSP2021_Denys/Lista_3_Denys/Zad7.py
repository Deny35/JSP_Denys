
N = int(input('Wprowadz N: '))
f1 = 0
f2 = 1


for i in range(0, N+1):
    print(f1)
    f = f2
    f2 = f2 + f1
    f1 = f




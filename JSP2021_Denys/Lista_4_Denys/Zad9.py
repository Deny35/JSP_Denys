def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    else:
        return 1 

x = int(input('Silnia: '))
if x<0:
    print('!BŁĄD!')
else:
    print(x,'!=',silnia(x))
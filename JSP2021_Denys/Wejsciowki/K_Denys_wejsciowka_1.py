x = range(3, 100, 3) # tworzy liste wielokrotnosci 3
x = list(x) # tworzy liste
print(x) # wypisuje liste
print('\n')
y = x # tworzy liste
del y [2:100:3] # usuwa co 3 
print(y) # wypisuje liste
print(sum(y)/len(y))# suma arytmetyczna
x = range(3, 100, 3) # tworzy liste wielokrotności 3
for i in x:
    print(i)# wypisuje liczby co 3
y = list(x)
del y [4:100:3] # usuwa co trzeci element
print(sum(y)/len(y)) # średnia arytmetyczna 
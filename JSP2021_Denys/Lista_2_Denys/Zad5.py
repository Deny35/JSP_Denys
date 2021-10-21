slowo = input('Wpisz słowo:  ')
pol = 'pies'
dl = int(len(slowo)/2)
nowe = slowo[0:dl]+ pol + slowo[(dl):]
print(nowe)

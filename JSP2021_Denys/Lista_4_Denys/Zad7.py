n = int(input("Ile wierszy wypisać?\n Ilośc: "))


def wypiszPascala(wierszy):
    lista = []
    while (wierszy > 0):
        for i in range(1, len(lista)):
            lista[i] = lista[i] + lista[i - 1]
        lista.append(1)
        txt = ''
        for x in range(0, int(wierszy/2)):
          txt += '\t'
        for a in enumerate(lista):
          if (wierszy % 2 == 1):
            txt += '  '
          txt += str(a[1]) + '\t'
        print(txt)
        wierszy = wierszy - 1

        
wypiszPascala(n)
def szyfrowanie(tekst, klucz):
    szyfr = ''
    for i in range (len(tekst)): 
        if (ord(tekst[i]) < 65 )or (ord(tekst[i]) > 90 and ord(tekst[i]) < 97):# sprawdza czy znak nie jest literą
            szyfr += chr(ord(tekst[i]))# zistawia bez zmian
        elif (ord(tekst[i]) < 97 and ord(tekst[i])  > 90) or (ord(tekst[i]) > 122): # sprawdza czy znak nie jest literą
            szyfr += chr(ord(tekst[i]))# zistawia bez zmian
        elif (ord(tekst[i]) >= 97 and ord(tekst[i]) <=122) or (ord(tekst[i]) >= 65 and ord(tekst[i]) <=90):# sprawdza czy znak jest literą
            if (ord(tekst[i]) > 97 and (ord(tekst[i]) + klucz > 122)) or (ord(tekst[i]) < 90 and (ord(tekst[i]) + klucz > 90)):# sprawdza czy po dodaniu klucza nie wychodzi za skale
                szyfr += chr((ord(tekst[i])) + klucz - 26)# zamienia litere i dodaje dodaje do ciągu
            else:
                szyfr += chr((ord(tekst[i])) + klucz)# zamienia litere i dodaje dodaje do ciągu
    return szyfr
                
def deszyfrowanie(tekst, klucz):
    dszyfr = ''
    for i in range (len(tekst)): 
        if (ord(tekst[i]) < 65 )or (ord(tekst[i]) > 90 and ord(tekst[i]) < 97):# sprawdza czy znak nie jest literą
            print('tak1')
            dszyfr += chr(ord(tekst[i]))# zistawia bez zmian
        elif (ord(tekst[i]) < 97 and ord(tekst[i]) > 90) or (ord(tekst[i]) > 122): # sprawdza czy znak nie jest literą
            print('tak2')
            dszyfr += chr(ord(tekst[i]))# zistawia bez zmian
        elif (ord(tekst[i]) >= 97 and ord(tekst[i]) <=122) or (ord(tekst[i]) >= 65 and ord(tekst[i]) <=90):# sprawdza czy znak jest literą
            if (ord(tekst[i]) > 97 and (ord(tekst[i]) - klucz > 122)) or (ord(tekst[i]) < 90 and (ord(tekst[i]) - klucz > 90)):# sprawdza czy po dodaniu klucza nie wychodzi za skale
                dszyfr += chr((ord(tekst[i])) - klucz + 26)# zamienia litere i dodaje dodaje do ciągu
            else:
                dszyfr += chr((ord(tekst[i])) - klucz)# zamienia litere i dodaje dodaje do ciągu
    return dszyfr
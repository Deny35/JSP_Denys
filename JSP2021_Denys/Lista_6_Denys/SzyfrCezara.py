def szyfrowanie(tekst, klucz):
    szyfr = ''
    for i in range (len(tekst)): 
        if ord(tekst[i]) < 97 or ord(tekst[i]) >122:
            szyfr += chr(ord(tekst))
        elif ord(tekst[i]) >= 97 and ord(tekst[i]) <= 122:
            if ord(tekst[i]) + klucz > 122:
                szyfr += chr(ord(tekst[i])) + klucz - 26
            else:
                szyfr += chr(ord(tekst[i])) + klucz
    return szyfr
                

tlumacz = { 'I':1, 'V':5, 'X':10, 'L':50,
               'C':100, 'D':500, 'M':1000}# słownik liczb rzymskich
def zamiana(lr):
    suma = 0
    lr = list(lr)# zmienia na liste
    #lr.insert(0,'end')
    ld = lr # przypisanie wartości 
    ld = list(ld) # zmiana na liste
    for i in range(0, len(lr)):
        if lr[len(lr)-i-1] in tlumacz:
            ld[i] = (tlumacz.get(lr[len(lr)-i-1]))#zmienia na liczbe 
               
    
    for i in range(0, len(lr)):
        if i == len(lr)-1:
            if ld[i] >= ld[i-1]:
                suma += ld[i]
            else:
                suma -= ld[i]
        elif i == 0:
            suma = ld[i]
            #if ld[i]>ld[i+1]:
             #   suma = -ld[i]
        else:
            if ld[i] >= ld[i-1]:
                suma += ld[i]
            else:
                suma -= ld[i]
    return(suma)    
    
    
    

n = input('Podaj liczbe(Należy wpisywać WIELKIMI literami!): ')
print(zamiana(n))

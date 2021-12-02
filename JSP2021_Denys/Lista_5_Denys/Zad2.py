tlumacz={-1:'', 0:'zero', 1:'jeden', 2:'dwa', 3:'trzy', 4:'cztery', 5:'pięć', 6:'sześć', 7:'siedem', 8:'osiem',
        9:'dziewięć', 10:'dziesięć', 11:'jedenaście', 12:'dwanaście', 13:'trzynaście', 14:'czternaście', 15:'piętnaście',
        16:'szesnaście', 17:'siedemnaście', 18:'osiemnaście', 19:'dziewiętnaście',20:'dwadzieścia',
        30:'trzydzieści', 40:'czterdzieści', 50:'pięćdziesiąt', 60:'sześćdziesiąt', 70:'siedemdziesiąt', 80:'osiemdziesiąt', 90:'dziewięćdziesiąt',
        100:'sto', 200:'dwieście', 300:'trzysta', 400:'czterysta', 500:'pięćset', 600:'sześćset', 700:'siedemset', 800:'osiemset', 900:'dziewięćset', 1000:'tysiąc'}#Przypożudkuje słową ich odpowednich w liczbach. Przed dwukropkie
                                                                 # jesy keyname, a po wartość jej przypisana

def zamiana(tys,set,dzi,jed):
    r = 0
    k = 0
    j = 0
    p = 0
    if(tys in tlumacz):
        r = (tlumacz.get(tys))#zmienia na liczbe
    if(set in tlumacz):
        k = (tlumacz.get(set))#zmienia na liczbe
    if(dzi in tlumacz):
       j = (tlumacz.get(dzi))#zmienia na liczbe
    if(jed in tlumacz):
       p = (tlumacz.get(jed))#zmienia na liczbe
    if(r == ''):
        print(k +' '+ j +' '+ p)
    elif(r == '' and k == '0'):
        print( j +' '+ p)
    elif(r == '' and k == '' and j == ''):
        print(p)
    else:
        print(r +' '+ k +' '+ j +' '+ p)


x = int(input("Podaj słownie liczbę: "))
if (x<20):
    d = -1 #ustawia wartość na pusta    
    c = -1 #ustawia wartość na pusta    
    a = -1 #ustawia wartość na pusta    
    b = x # od 0 do 20
if (x>=20 and x<100):
    d = -1 #ustawia wartość na pusta    
    c = -1 #ustawia wartość na pusta    
    a = int((x/10))*10# oblicza całkowite dziesiątki
    b = x%10# oblicza od 1-9
    if b == 0:
         b = -1
if(x>=100 and x<1000):
     d = -1 #ustawia wartość na pusta    
     c = int((x/100))*100# oblicza całkowite setki
     a = int(((x%100)/10))*10# oblicza całkowite dziesiątki
     b = x%10# oblicza od 1-9
     if b == 0:
        b = -1
     if a == 0:
        a = -1
if(x>=1000 and x<2000):
     d = int((x/1000))*1000 # oblicza człkowite tysiące
     c = int(((x%d)/100))*100# oblicza całkowite setki
     a = int(((x%100)/10))*10# oblicza całkowite dziesiątki
     b = x%10 # oblicza od 1-9
     if b == 0:
         b = -1
     if a == 0:
         a = -1
zamiana(d,c,a,b)
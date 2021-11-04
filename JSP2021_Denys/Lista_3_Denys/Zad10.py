x = []
for i in range(100,401):
    c = int((i/100))# oblicza całkowite setki
    a = int(((i%100)/10))# oblicza całkowite dziesiątki
    b = i%10# oblicza od 1-9
    if c%2==0 and a%2==0 and b%2==0:
        x.append(i)
        #print(i, end=", ")

print(x)
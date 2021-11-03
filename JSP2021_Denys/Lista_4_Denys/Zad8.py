n = int((input("Ilość elementow: ")))

a = 1
suma = 0
for i in range(1,n+1):
    c = a/(i)
    suma += c 

print("Suma elementów to: ", suma)
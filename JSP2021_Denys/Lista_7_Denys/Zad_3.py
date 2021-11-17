def sort(lista):
    n = len(lista)
    while n > 1:
        zamien = False
        for l in range(0, n-1):
            if lista[l] > lista[l+1]:
                lista[l], lista[l+1] = lista[l+1], lista[l]
                zamien = True  
        n -= 1
        if zamien == False: break
    
    return lista

import time
import random

a = []

for i in range (1,101):
    r = random.randint(0, 20)
    a.append(r)

start_time = time.time()
# sortowanie
print(sort(a))

stop_time = time.time()
print(stop_time - start_time)

b = []

for i in range (1,201):
    r = random.randint(0, 20)
    b.append(r)

start_time = time.time()
# sortowanie
print(sort(b))

stop_time = time.time()
print(stop_time - start_time)

c = []

for i in range (1,301):
    r = random.randint(0, 20)
    c.append(r)

start_time = time.time()
# sortowanie
print(sort(c))

stop_time = time.time()
print(stop_time - start_time)
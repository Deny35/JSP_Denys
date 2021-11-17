def Insert_sort(A):
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j>=0 and A[j]>klucz:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    return(A) 

import random
import time

a = []

for i in range (1,101):
    r = random.randint(0, 20)
    a.append(r)

start_time = time.time()
# sortowanie
print(Insert_sort(a))

stop_time = time.time()
print(stop_time - start_time)

b = []

for i in range (1,201):
    r = random.randint(0, 20)
    b.append(r)

start_time = time.time()
# sortowanie
print(Insert_sort(b))

stop_time = time.time()
print(stop_time - start_time)

c = []

for i in range (1,301):
    r = random.randint(0, 20)
    c.append(r)

start_time = time.time()
# sortowanie
print(Insert_sort(c))

stop_time = time.time()
print(stop_time - start_time)
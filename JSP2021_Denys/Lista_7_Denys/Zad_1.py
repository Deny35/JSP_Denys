import time

n = int(input('Podaj długość ciągu: '))

f1 = 0
f2 = 1

start_time = time.time()

for i in range(0, n):
    f = f2
    f2 = f2 + f1
    f1 = f
    
print(f1)

end_time = time.time()
print (end_time - start_time)

def fibo(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fibo(n-1)+fibo(n-2)

start_time = time.time()

print(fibo(n))

end_time = time.time()
print (end_time - start_time)
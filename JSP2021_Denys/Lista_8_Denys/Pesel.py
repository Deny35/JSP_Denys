import time
import random

def pesel_gen():
    sex = input('Chłopiec (M) czy dziewczynka (F): ')

    timee  = time.localtime()
    day = str(timee.tm_mday)
    month = str(timee.tm_mon)
    year = str(timee.tm_year)
    z1 = str(random.randint(0, 9))
    z2 = str(random.randint(0, 9))
    z3 = str(random.randint(0, 9))

    if sex == 'M':
        x = random.randint(0, 9)
        while x%2 == 0:
            x = random.randint(0, 9)
        x = str(x)
    else:
        x = random.randint(0, 9)
        while x%2 == 1:
            x = random.randint(0, 9)
        x = str(x)
    #q = str(-1*(int(int((1*int((year%100)/10) + 3*(year%10) + 7*int(month/10) + 9*(month%10) + 1*int(day/10) + 3*(day%10) + 7*z1 + 9*z2 + 1*z3 + 3*x)%100)%10)-10))
    q = str(1*int(year[2]) + 3*int(year[3]) + 7*int(month[0]) + 9*int(month[1]) + 1*int(day[0]) + 3*int(day[1]) + 7*int(z1) + 9*int(z2) + 1*int(z3) + 3*int(x))
    print(q)
    q = int(q[len(q)-1])
    print(q)
    q = str(q-10)
    q = q[len(q)-1]
    pesel =(year[2:] + month + day + z1 + z2 + z3 + x + q)
    return pesel + '\n'
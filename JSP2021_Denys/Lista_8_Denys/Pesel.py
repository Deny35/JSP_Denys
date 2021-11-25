
import random

def pesel_gen():
    

    year = (random.randint(1922, 2021))
    month = (random.randint(1, 12))
    if(month%2 == 1):
        day = random.randint(1, 31)
    elif(month == 2 and year%4 == 0):
        day = random.randint(1, 29)
    elif(month == 2 and year%4 != 0):
        day = random.randint(1, 28)
    else:
        day = random.randint(1, 30)
    
    if(day<10):
        day = str(day)
        day = '0' + day
    else:
        day = str(day)

    if(month<10):
        month = str(month)
        month = '0' + month
    else:
        month = str(month)

    year= str(year)

    z1 = str(random.randint(0, 9))
    z2 = str(random.randint(0, 9))
    z3 = str(random.randint(0, 9))
    sex = str(random.randint(0, 1))
    if sex == 1:
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

    q = int(q[len(q)-1])
 
    q = str(q-10)
    q = q[len(q)-1]
    pesel =(year[2:] + month + day + z1 + z2 + z3 + x + q)
    return pesel + '\n'
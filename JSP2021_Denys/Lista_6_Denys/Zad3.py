n=int(input("Podaj n wyrazow ciagu:"))

def lookAndSay(x):
    result=[]
    i=0
    while i < len(x):
        count=1
        while i + 1 <len(x) and x[i] == x[i+1]:
            i+=1
            count+=1
        result.append(str(count)+x[i])
        i+=1
    return ''.join(result)

x="1"
for i in range(n):
    x=lookAndSay(x)
    print(x)


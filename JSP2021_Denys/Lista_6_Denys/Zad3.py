#def lookandsay(n):
ciag = ""
i = 1
a = 0
n = '11121'
while i < len(n):
    if n[i-1] != n[i]:
        licz = n[a:i].count(n[a:i])
        a = i- 1
        licz = str(licz)
        ciag  = ciag + licz + n[a]
    i += i
print(ciag)

#pierwszy  = "1"
#for i in range(3):
#    print (pierwszy)
#    pierwszy = lookandsay(pierwszy)

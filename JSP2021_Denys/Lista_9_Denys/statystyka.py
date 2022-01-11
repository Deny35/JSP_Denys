import sys, re
#import numpy
import fileinput

def oblicz(info):
    info = str(info)
    info = re.findall('\w+', info) 
    print(info)
    dane = [int(i) for i in info if type(i) == int or i.isdigit()] 
    wyniki = [numpy.mean(dane), numpy.std(dane), numpy.var(dane)]
    return wyniki

if len(sys.argv) == 2:
    for line in fileinput.input():
        x =line.rstrip()
else:
    print (len(sys.argv))
    x = sys.argv[1:]
print(x)
#wyniki = oblicz(x)
#print("srednia: ", wyniki[0], "odchylenie standardowe: ", wyniki[1], "wariancja: ", wyniki[2])

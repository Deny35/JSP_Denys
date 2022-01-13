import sys, re
import numpy

def operacje(liczby):
    dane = [int(i) for i in liczby if i.isdigit()]  
    print(dane)
    wyniki = [numpy.mean(dane), numpy.var(dane), numpy.std(dane)]
    return wyniki

import os


def open_file(path):
   
   if not os.path.exists(path):
        pass    
   else:
        while open(path):
            return [int(x) for x in path]
  

if len(sys.argv) == 2:
    liczby = open_file(sys.argv[1])
            
    
else:
    liczby = sys.argv[1:]
wyniki = operacje(liczby)
print("srednia: ", wyniki[0], "wariancja: ", wyniki[1] ,"odchylenie standardowe: ", wyniki[2])

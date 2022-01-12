import sys, re
import numpy

def operacje(info):
    dane = [int(i) for i in info if type(i) == int or i.isdigit()]  
    wyniki = [numpy.mean(dane), numpy.std(dane), numpy.var(dane)]
    return wyniki

import os


def open_file(path):
   
   if not os.path.exists(path):
        print("Nie istnieje")    
   else:
        print(path)
        print("Plik istnieje")
        file_open = open(path, 'r', encoding='utf-8', errors='ignore') 
        file_text = file_open.read()
        file_open.close()
        return file_text
  

if len(sys.argv) == 2:
            print(sys.argv[1])
            x = open_file(sys.argv[1])
            print(x)
            
    
else:
    x = sys.argv[1:]
wyniki = operacje(x)
print("srednia: ", wyniki[0], "odchylenie standardowe: ", wyniki[1], "wariancja: ", wyniki[2])

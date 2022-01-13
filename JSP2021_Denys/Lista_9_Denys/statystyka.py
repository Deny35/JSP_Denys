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
        print("Nie istnieje")    
   else:
        print(path)
        print("Plik istnieje")
        file_open = open(path, 'r', encoding='utf-8', errors='ignore') 
        file_text = file_open.read()
        file_open.close()
        return file_text
  

if len(sys.argv) == 2:
    liczby = open_file(sys.argv[1])
            
    
else:
    liczby = sys.argv[1:]
wyniki = operacje(liczby)
print("srednia: ", wyniki[0], "wariancja: ", wyniki[1] ,"odchylenie standardowe: ", wyniki[2])

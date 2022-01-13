import os
import numpy
import sys, re
#indeks: 326321

def operacje(liczby, wybor):
    dane = [int(i) for i in liczby if i.isdigit()]  
    
    if wybor=='--mean':
        wynik = 'Średnia= ' + str(numpy.mean(dane))
    
    if wybor=='--median':
        wynik = 'Mediana= ' + str(numpy.median(dane))
    
    return wynik


def open_file(path):
   
   if not os.path.exists(path):
       pass 
   else:
        file_open = open(path, 'r', encoding='utf-8', errors='ignore') 
        file_text = file_open.readlines()
        file_open.close()
        textWithout = []
        for element in file_text:
            textWithout.append(element.strip())
        return textWithout

file = sys.argv[1]
numbers = open_file(file)
choice = sys.argv[2]
print(choice) 
wyniki = operacje(numbers, choice)
print(wyniki)

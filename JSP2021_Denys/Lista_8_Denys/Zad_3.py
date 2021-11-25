import Pesel
import os
from os import path

path_file = 'pesel.txt'
file_save = open(path_file,'w+' )

for i in range (0,10):
    pesel = (Pesel.pesel_gen())
    file_save.write(pesel)

file_save.close()

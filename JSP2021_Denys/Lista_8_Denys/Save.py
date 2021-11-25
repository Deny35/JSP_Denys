import time
import os
from os import path

def save_file(text, key):
    path = input("Podaj nazwe folderu: ")
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print("Nie udalo sie stworzyc folderu")
        else:
            print("Stworzono folder")
    
    if os.path.exists(path):
        timee  = time.localtime()
        day = timee.tm_mday
        month = timee.tm_mon
        year = timee.tm_year
        path_file = path + '\plik_zaszyfrowany'+ str(key) + '_' + str(year) + '-' + str(month) + '-' + str(day)+'.txt'
        file_save = open(path_file,'w+' )
        file_save.write(text)
        file_save.close()    

    if os.path.exists(path_file):
        print('Plik zapisano')
    else:
        print('Plik nie zapisany')

def save_file_z2(text, key):
    path = input("Podaj nazwe folderu: ")
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print("Nie udalo sie stworzyc folderu")
        else:
            print("Stworzono folder")
    
    if os.path.exists(path):
        timee  = time.localtime()
        day = timee.tm_mday
        month = timee.tm_mon
        year = timee.tm_year
        path_file = path + '\deszyfrowany'+ str(key) + '_' + str(year) + '-' + str(month) + '-' + str(day)+'.txt'
        file_save = open(path_file,'w+' )
        file_save.write(text)
        file_save.close()    

    if os.path.exists(path_file):
        print('Plik zapisano')
    else:
        print('Plik nie zapisany')
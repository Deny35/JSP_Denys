import time
import os

def save_file(text, key,path_file):
    #path_file =  os.getcwd()
    path_f = input("Podaj nazwe folderu: ")
    path = path_file + '\\' + path_f
    print(path)
    if not os.path.exists(path):
        try:
            os.makedirs(path)
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
        file_save = open(path_file,'w+', encoding='utf-8' )
        file_save.write(text)
        file_save.close()    

    if os.path.exists(path_file):
        print('Plik zapisano')
    else:
        print('Plik nie zapisany')

############################################################
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
##############################################################################################
def save_file_z4(pesels, day, month, year, sex):
    path_file = os.getcwd() + '\pesel_odzyfrowany.txt'
    print(pesels)
    print(month)
    file_save = open(path_file,'w+' )
    for i in range (0,10):
        file_save.write((pesels[i] + ':\n' + day[i] + '-' + month[i] + '-' + year[i] + '\t' + sex[i]+'\n'))
    file_save.close() 
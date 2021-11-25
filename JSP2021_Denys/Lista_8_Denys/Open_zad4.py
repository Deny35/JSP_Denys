import os
from os import path

def open_file(path):
   file_text = []
   if not os.path.exists(path):
        print("Nie istnieje")
        
   else:
        print(path)
        print("Plik istnieje")
        file_open = open(path, 'r', encoding='utf-8') 
        for i in range (0,10):
            x = file_open.readline()
            x = x.strip('\n')
            file_text.append(x)
        file_open.close()
        return file_text
    
     
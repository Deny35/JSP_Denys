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
    


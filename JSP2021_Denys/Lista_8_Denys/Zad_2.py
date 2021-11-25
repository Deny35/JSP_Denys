import SzyfrCezara
import fnmatch
import os 
import Open
import Save

path_encrypted = input('Podaj ścieżke pliku: ')

i = 0

for file in os.listdir(path_encrypted):
    if fnmatch.fnmatch(file, '*.txt'):
       key = file[17]
       if file[18] == 0:
           key = 10
    file_text =  path_encrypted +'\\' + file
    encrypted_text = Open.open_file(file_text)
    #unencrypted_text = SzyfrCezara.deszyfrowanie(encrypted_text, key)
    Save.save_file_z2(encrypted_text, key)
    
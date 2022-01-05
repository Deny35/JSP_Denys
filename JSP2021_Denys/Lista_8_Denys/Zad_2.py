import SzyfrCezara
import fnmatch
import os 
import Open
import Save

path_encrypted = input('Podaj sciezke pliku: ')

i = 0

for file in os.listdir(path_encrypted):
    if fnmatch.fnmatch(file, 'plik_zaszyfrowany*.txt'):
       print (file)
       key = file[17]
       if file[18] == 0:
           key = 10
       print(key)
       file_text =  path_encrypted +'\\' + file
       encrypted_text = Open.open_file(file_text)
       unencrypted_text = SzyfrCezara.deszyfrowanie(encrypted_text, int(key))
       print(unencrypted_text)
       Save.save_file_z2(unencrypted_text, key, path_encrypted)
    
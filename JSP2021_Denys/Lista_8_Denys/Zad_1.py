import SzyfrCezara
import Open
import Save


#C:\studia_s3\L_Python\JSP2021_Denys\Lista_8_Denys\PLIT_DO_SZYFROWANIA.txt
path = input('Podaj ścieże do pliku: ')
file = input('Podaj nazwę pliku z rozszerzeniem: ')
unencrypted_text = Open.open_file(path + '\\' + file)

key = int(input('Podaj klucz syfrowania od 1 do 10:'))
if key > 10:
    while key > 10:
        print('Klucz nie prawidłowy!')
        key = int(input('Podaj klucz syfrowania od 1 do 10:'))
elif key < 1:
    while key < 1:
        print('Klucz nie prawidłowy!')
        key = int(input('Podaj klucz syfrowania od 1 do 10:'))
encrypted_text = SzyfrCezara.szyfrowanie(unencrypted_text, key)


Save.save_file(encrypted_text, key, path)

import SzyfrCezara
import time
import os
from os import path


plik = open('C:\studia_s3\L_Python\JSP2021_Denys\Lista_8_Denys\PLIT_DO_SZYFROWANIA.txt', 'r', encoding='utf-8')
try:
	tekst = plik.read()
finally:
	plik.close()

#print(tekst)

klucz = int(input('Podaj klucz syfrowania:'))
szyfr = SzyfrCezara.szyfrowanie(tekst, klucz)

#print(szyfr)

timee  = time.localtime()
day = timee.tm_mday
month = timee.tm_mon
year = timee.tm_year

name_file = ('plik_do_szyfrowania'+ str(klucz) + '_' + str(year) + '-' + str(month) + '-' + str(day)+'.txt')
print(name_file)
a = os.path.isfile(name_file)
print(a)

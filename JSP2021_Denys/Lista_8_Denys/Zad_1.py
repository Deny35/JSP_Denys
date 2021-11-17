import SzyfrCezara
import time


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

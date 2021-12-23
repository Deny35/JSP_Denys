import urllib.request
url = input('Podaj URL:  ')

try:  
    urllib.request.urlopen(url)
    print('Strona istnieje!')
except:
    print('Strona nie iestnieje!')

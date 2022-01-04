from bs4 import BeautifulSoup
from requests import get

url = 'https://www.nbp.pl/home.aspx?f=/kursy/kursya.html'

page = get(url)

bs = BeautifulSoup(page.content, 'html.parser')

a = bs.find('tbody')
waluta = []
wartosc = []
licz = 0
for i in a:
    if len(i)>=2:
        b = i.find_all('td', class_="right")
        for i in b:
            licz += 1
            if licz%2 == 0:
                if count > 0:
                    bufor1 = float((i.get_text().replace(',','.')))/(10**count)
                    wartosc.append(bufor1)
                else:
                    wartosc.append(float((i.get_text().replace(',','.'))))

            else:
                bufor2 = (i.get_text().replace('1','').replace(' ',''))
                count = bufor2.count('0')
                waluta.append((i.get_text().replace('1','').replace('0','').replace(' ','')))
        licz = 0




print(['THB', 'USD', 'AUD', 'HKD', 'CAD', 'NZD', 'SGD', 'EUR', 'HUF', 'CHF', 'GBP', 'UAH', 'JPY', 'CZK', 'DKK', 'ISK', 'NOK', 'SEK', 'HRK', 'RON', 'BGN', 'TRY', 'ILS', 'CLP', 'PHP', 'MXN', 'ZAR', 'BRL', 'MYR', 'RUB', 'IDR', 'INR', 'KRW', 'CNY', 'XDR'])
klijent = input('Podaj walute: ')
index = waluta.index(klijent)
kwota = int(input('Podaj kwote: '))

print(kwota*wartosc[index])



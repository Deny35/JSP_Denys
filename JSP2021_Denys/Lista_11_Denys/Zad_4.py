import re

text = input('Podaj tekst:   ')
print(re.findall("[ae]\w+", text))

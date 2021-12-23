import re

text = input('Podaj tekst:   ')
print(re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text))

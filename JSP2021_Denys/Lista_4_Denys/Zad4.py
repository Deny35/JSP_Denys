n = int(input("Podaj numer elementu: "))
a1 = int(input("Podaj 1 element ciagu: "))
q = int(input("Podaj q: "))

def wyraz_ciag():#Funkcja zwracająca warośc elementu
    an = a1 * q ** (n-1)
    return an

print(wyraz_ciag())

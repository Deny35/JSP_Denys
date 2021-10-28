R = int(input("Podaj R: "))
G = int(input("Podaj G: "))
B = int(input("Podaj B: "))

R = R/255
G = G/255
B = B/255

Cmax = max(R, G, B)
Cmin = min(R, G, B)
d = Cmax - Cmin

if Cmax == Cmin:
    h = 0
elif Cmax == R:
    h = (60 * ((G - B)/d) + 360) % 360
elif Cmax == G:
    h = (60 * ((B - R)/d) + 120) % 360
elif Cmax == B:
    h = (60 * ((R - G)/d) + 240) % 360

if Cmax == 0:
    s = 0
else:
    s = (d/Cmax) * 100

v = Cmax * 100

print(h,chr(176),' ',s,'%  ',v,'%  ')
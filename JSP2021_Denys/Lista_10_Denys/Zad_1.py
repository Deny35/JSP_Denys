class Kolo:
    def __init__(self, r):
        self.r = r
        
    def pole(self):
        import math
        return (math.pi*self.r**2)

    def obwod(self):
        import math
        return (2*self.r*math.pi)

klasa = Kolo(3)
print(klasa.pole())
print(klasa.obwod())
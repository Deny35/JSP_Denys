class Lista:
    def __init__(self,set):
        self.set = set
    def podlista(self):
        i = 0
        j = 1
        k = 2
        subset = []
        bufor_list = []
        while i < len(self.set)-1:
            while j < len(self.set)-1:
                while k <= len(self.set)-1:
                    if self.set[i] + self.set[j] + self.set[k] == 0:
                        bufor_1 = self.set[i]
                        bufor_2 = self.set[j]
                        bufor_3 = self.set[k]
                        bufor_list.append((bufor_1, bufor_2, bufor_3))
                        self.set.remove(bufor_1)
                        self.set.remove(bufor_2)
                        self.set.remove(bufor_3)
                        i = 0
                        j = 1
                        k = 2
                        subset.append(bufor_list)
                        break
                    else:
                        k += 1
        return bufor_list                
                        
                    

a = [1,1,-1,3,-2,-2]
clasa = Lista(a)
print(clasa.podlista())

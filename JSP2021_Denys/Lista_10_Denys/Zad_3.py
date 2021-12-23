class Lista:
    def podlista(self, n):
        i = 0
        j = 1
        k = 2
        subset = []
        bufor_list = []
        while i < len(n)-1:
            while j < len(n)-1:
                while k <= len(n)-1:
                    if n[i] + n[j] + n[k] == 0:
                        bufor_1 = n[i]
                        bufor_2 = n[j]
                        bufor_3 = n[k]
                        bufor_list.append((bufor_1, bufor_2, bufor_3))
                        n.remove(bufor_1)
                        n.remove(bufor_2)
                        n.remove(bufor_3)
                        i = 0
                        j = 1
                        k = 2
                        subset.append(bufor_list)
                        break
                    else:
                        k += 1
        return bufor_list                
                        
                    

a = [1,1,-1,3,-2,-2]
clasa = Lista()
print(clasa.podlista(a))

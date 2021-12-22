class Lista:
    def podlista(self, n):
        print(n)
        i = 0
        j = 1
        k = 2
        while i < len(n)-1:
            print(n[i])
            while j < len(n)-1:
                print(n[j])
                while k <= len(n)-1:
                    print(n[k])
                    if n[i] + n[j] + n[k] == 0:
                        print('tak')
                        bufor_1 = n[i]
                        bufor_2 = n[j]
                        bufor_3 = n[k]
                        n.remove(bufor_1)
                        n.remove(bufor_2)
                        n.remove(bufor_3)
                        print(n)
                        
                        
                    

a = [1,-2,1]
clasa = Lista()
clasa.podlista(a)
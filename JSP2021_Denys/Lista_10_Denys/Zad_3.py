class Listy:

    def podlisty(self, n):
        lista_1 = n
        p_lista = []
        print(n)
        for j in range(len(n)):
            for i in range(1,len(n)):
                for a in range(2,len(n)):
                    if a != j and a != i and i != j:
                        if n[j] + n[i] + n[a] == 0:
                            print(j)
                            print(i)
                            print(a)
                            bufor_1 = n[i] 
                            bufor_2 = n[j]
                            bufor_3 = n[a]
                            print('---------')
                            bufor = list(str(n[i]) + str(n[j]) +str(n[a]))
                            n.remove(bufor_1)
                            n.remove(bufor_2)
                            n.remove(bufor_3)
                            p_lista.append(bufor)
                            print(p_lista)
                            print(n)
                            i=0
                            j=0
                            a=0

a = [1,-2,1,2,2,-4]
clasa = Listy()
clasa.podlisty(a)







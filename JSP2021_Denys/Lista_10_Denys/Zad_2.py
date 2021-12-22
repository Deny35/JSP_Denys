class Lista:
    
    def podlisty(self, lista):
        print('przed')
        p_lista = [[]]
        print('po')
        for i in range(len(lista)):
            bufor = []
            for j in range(1,len(lista)):
                bufor = str(lista[i])                
                
li = Lista()
#print(li.podlisty([1,2,3]))

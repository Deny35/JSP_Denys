'''
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
'''

def get_power_set(s):
  power_set=[[]]
  for elem in s:
    # iterate over the sub sets so far
    for sub_set in power_set:
      # add a new subset consisting of the subset at hand added elem
      power_set=power_set+[list(sub_set)+[elem]]
  return power_set

#print(map(get_power_set([1,2,3])))
#alo = get_power_set([1,2,3])
#print(alo[0])
belo = [[],[3],[1],[2,3],[3]]
print(belo.sort(key=len))
class clas1:
  def __init__(self,set):
    self.set = set
  
  def get_power_set(self):
    power_set=[[]]
    for elem in self.set:
      for sub_set in power_set:
        power_set=power_set+[list(sub_set)+[elem]]
    return power_set


zbor = clas1([1,2,3])
x = zbor.get_power_set()
x.sort(key=len)
print(x)
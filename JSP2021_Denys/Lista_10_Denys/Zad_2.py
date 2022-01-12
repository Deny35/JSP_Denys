class clas1:
  def get_power_set(s):
    power_set=[[]]
    for elem in s:
      for sub_set in power_set:
        power_set=power_set+[list(sub_set)+[elem]]
    return power_set


zbor = clas1()
x = zbor.get_power_set([1,2,3])
x.sort(key=len)
print(x)
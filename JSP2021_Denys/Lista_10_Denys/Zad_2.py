def get_power_set(s):
  power_set=[[]]
  for elem in s:

    for sub_set in power_set:

      power_set=power_set+[list(sub_set)+[elem]]
  return power_set

belo = [[],[3],[1],[2,3],[3]]
print(belo.sort(key=len))

ini_list = [[1, 2, 3], [1, 2], [1, 2, 3, 4],
                [1, 2, 3, 4, 5], [2, 4, 6]]
  

print ("initial list", str(ini_list))
  

ini_list.sort(key = len)
  

print("final list", str(ini_list))
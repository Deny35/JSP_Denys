x = range(3, 100, 3)
for i in x:
  print(i) 
y = list(x)
del y [4:100:3]
print(sum(y)/len(y))

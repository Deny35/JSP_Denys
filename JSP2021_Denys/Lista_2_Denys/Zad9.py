from itertools import chain
a = [[2, 4, 4], [1, 5, 6], [7, 9, 0]]
ab = list(chain(*a))
print(ab)
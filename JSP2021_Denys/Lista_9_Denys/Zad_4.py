import matplotlib.pyplot as plt

language = ['Python',  'C', 'Java', 'C++', 'C#', 'Visual Basic', 'JavaScript', 'Assembly language', 'SQL', 'Swift' ]
ratings = [12.9, 11.8, 10.2, 7.7, 6.4, 5.4, 2.3, 2.3, 1.8, 1.8]

plt.figure(figsize=(18, 5))
plt.bar(language, ratings)
plt.xlabel("Języki programowania")
plt.ylabel("Popularność w procętach")
plt.show()

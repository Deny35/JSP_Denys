import matplotlib.pyplot as plt

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

language = ['Python',  'C', 'Java', 'C++', 'C#', 'Visual Basic', 'JavaScript', 'Assembly language', 'SQL', 'Swift' ]
ratings = [12.9, 11.8, 10.2, 7.7, 6.4, 5.4, 2.3, 2.3, 1.8, 1.8]

plt.figure(figsize=(18, 5))
plt.bar(language, ratings)
addlabels(language, ratings)
plt.xlabel("Języki programowania")
plt.ylabel("Popularność w procętach w %")
plt.show()

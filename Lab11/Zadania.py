import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Zadanie 1
#Wykres Liniowy

sns.set(rc={'figure.figsize': (8, 8)})
sns.lineplot(x=[1, 2, 3, 4], y=[1, 4, 9, 16],
             label='linia nr1', color='red', marker='o', linestyle=':')
sns.lineplot(x=[1, 2, 3, 4], y=[2, 5, 10, 17],
             label='linia nr2', color='green', marker='^', linestyle=':')
plt.xlabel('oś x')
plt.ylabel('oś y')
plt.title('Wykres liniowy')

plt.show()

#Zadanie 2
#Wykres liniowy z wykorzystaniem serii danych

s = pd.Series(np.random.randn(1000))
s = s.cumsum()
sns.set()
wykres = sns.relplot(kind='line', data=s, label='linia')
wykres.fig.set_size_inches(8, 6)
wykres.fig.suptitle('Wykres liniowy losowych danych')
wykres.set_xlabels('indeksy')
wykres.set_ylabels('wartości')
wykres.add_legend()
wykres.figure.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9)

plt.show()

#Zadanie 3
#Wykers liniowy z wykorzystaniem ramki danych

sns.set()
df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')

print(df)
wykres = sns.lineplot(data=df, x=df.index, y='sepal length', hue='class')
wykres.set_xlabel('indeksy')
wykres.set_title('Wykres liniowy danych z Iris dataset')
wykres.legend(title='Rodzaj kwiatu')

plt.show()


#Zadanie 4
#Wykres punktowy

sns.set()
data = {'a': np.arange(10),
        'c': np.random.randint(0, 50, 10),
        'd': np.random.randn(10)}
data['b'] = data['a'] + 10 * np.random.randn(10)
data['d'] = np.abs(data['d']) * 100
print(data['c'])
print(data['d'])
df = pd.DataFrame(data)
plot = sns.relplot(data=df, x="a", y="b", hue="c", palette='bright', size="d", legend=True)
plot.fig.set_size_inches(6, 6)
plot.set(xticks=data['a'])

plt.show()

#Zadanie 5
#Wykres kolumnowy

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'AmerykaPołudniowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}
df = pd.DataFrame(data)
sns.set()# plot = sns.catplot(data=df, x='Kontynent', y='Populacja', kind='bar', ci=None, hue='Kontynent', estimator=np.sum,
#                    dodge=False, palette=['red', 'green', 'yellow'], legend_out=False)
# plot.fig.set_size_inches(7, 6)
# plot.add_legend(title='Populacja na kontynentach', loc='upper right')
# plot.fig.suptitle('Populacja na kontynentach')
#
plot = sns.barplot(data=df, x='Kontynent', y='Populacja',
                   ci=None, hue='Kontynent', estimator=np.sum,
                   dodge=False, palette=['red', 'green', 'yellow'])
plot.legend(title='Populacja na kontynentach')
plot.set(title='Wykres słupkowy')

plt.show()
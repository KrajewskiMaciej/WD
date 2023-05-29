import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1
#Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ε[1, 20].
# Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

x = np.arange(1, 21, 1)

plt.plot(x, 1/x, label='f(x) = 1/x')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.axis([0, 20, 0, 1])

plt.legend()

plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')

plt.show()


#Zadanie 2
#Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.


x = np.arange(1, 21, 1)

plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x' )

plt.xlabel('x')
plt.ylabel('f(x)')

plt.axis([0, 20, 0, 1])

plt.legend()

plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')

plt.show()


#Zadanie 3
#Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ε[0, 30] z krokiem 0.1.
# Dodaj etykiety i legendę do wykresu.

x = np.arange(0, 30, .1)

plt.plot(x, np.sin(x), 'b', label='sin(x)')
plt.plot(x, np.cos(x), 'r', label='cos(x)')

plt.xlabel('x')

plt.ylabel('sin(x) cos(x)')

plt.legend(loc='upper right')

plt.title('Wykres sin(x), cos(x)')

plt.show()

#Zadanie 4
#Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris)
# wygeneruj wykres punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’,
# dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną
# z różnicy wartości poszczególnych elementów wektorów x oraz y.

df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
print(df)

colors = np.random.randint(0, 50, len(df.index))

scale = np.abs(df['sepal length'] - df['sepal width'])


plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)

plt.xlabel('sepal length')
plt.ylabel('sepal width')

plt.show()


#Zadanie 5
#Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8.
# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny).
# Dodaj do wykresów stosowne etykiety.
# Poustawiaj różne kolory dla wykresów.
# 1 wykres –wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
# 2 wykres –wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna.
#   Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# 3 wykres –wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

xlsx = pd.ExcelFile('imiona.xlsx')

df = pd.read_excel(xlsx, header=0)

print(df)

plt.subplot(1, 3, 1)

grouped = df.groupby('Plec')

etykiety = list(grouped.groups.keys())
wartosci = list(grouped.agg('Liczba').sum())

plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
plt.xlabel('Płeć')
plt.ylabel('Liczba narodzonych dzieci')

plt.subplot(1, 3, 2)
x = df['Rok'].unique()

kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values

plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")

plt.xlabel('Rok')


plt.subplot(1, 3, 3)

x = df['Rok'].unique()
y = df.groupby('Rok').agg('Liczba').sum()

plt.bar(x, y)
plt.xlabel('Rok')

plt.subplots_adjust(wspace=0.85)
plt.show()

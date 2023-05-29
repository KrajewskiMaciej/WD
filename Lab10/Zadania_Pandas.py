import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Zadanie 1
#Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

df = pd.read_excel('imiona.xlsx')

dzieci_na_rok = df.groupby('Rok')['Liczba'].sum()

plt.plot(dzieci_na_rok.index, dzieci_na_rok.values, marker='o')

plt.title('Liczba urodzonych dzieci dla każdego roku')
plt.xlabel('Rok')
plt.ylabel('Liczba urodzeń')

plt.show()

#Zadanie 2
#Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

urodzenia_plec = df.groupby('Plec')['Liczba'].sum()

plt.bar(urodzenia_plec.index, urodzenia_plec.values)

for i, value in enumerate(urodzenia_plec.values):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.title('Liczba urodzonych chłopców i dziewczynek')
plt.xlabel('Plec')
plt.ylabel('Liczba urodzeń')

plt.show()

#Zadanie 3
#Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.

ostatnie_5_lat = df[df['Rok'] >= df['Rok'].max() - 4]

urodzenia_plec = ostatnie_5_lat.groupby('Plec')['Liczba'].sum()

plt.pie(urodzenia_plec, labels=urodzenia_plec.index, autopct='%1.1f%%')

plt.title('Ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach')

plt.show()

#Zadanie 4
#Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).

df1 = pd.read_csv('zamowienia.csv')

ilosc_zamowien_sprzedawcy = df1['Sprzedawca'].value_counts()
ilosc_zamowien_sprzedawcy = df1['Sprzedawca'].value_counts()

plt.bar(ilosc_zamowien_sprzedawcy.index, ilosc_zamowien_sprzedawcy.values)

for i, value in enumerate(ilosc_zamowien_sprzedawcy.values):
    plt.text(i, value, str(value), ha='center', va='bottom')

plt.xticks(rotation=90)

plt.title('Ilość złożonych zamówień przez sprzedawców')
plt.xlabel('Sprzedawca')
plt.ylabel('Ilość zamówień')

plt.tight_layout()
plt.show()



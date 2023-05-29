
#Zadanie 1
#Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx
import pandas as pd

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print("Zadanie 1")
print(df.head())

#Zadanie 2
#Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
# •tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# •tylko rekordy gdzie nadane imię jest takie jak Twoje
# •sumę wszystkich urodzonych dzieci w całym danym okresie,
# •sumędzieci urodzonych w latach 2000-2005•sumę urodzonych chłopców i dziewczynek,
# •najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# •najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,
print("Zadanie 2")

df_gt_1000 = df[df['Liczba'] > 1000]

df_my_name = df[df['Imie'] == 'MACIEJ']

suma_urodzonych = df['Liczba'].sum()

suma_urodzonych_2000_2005 = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Liczba'].sum()

suma_chlopcow = df[df['Plec'] == 'M']['Liczba'].sum()
suma_dziewczynek = df[df['Plec'] == 'K']['Liczba'].sum()

najpopularniejsze_imiona = df.groupby(['Rok', 'Plec']).apply(lambda x: x.nlargest(1, 'Liczba')).reset_index(drop=True)

najpopularniejsze_imiona_cały_okres = df.groupby(['Imie', 'Plec']).sum().reset_index().sort_values(by='Liczba', ascending=False).groupby('Plec').first()

print("Rekordy, gdzie liczba nadanych imion była większa niż 1000 w danym roku:")
print(df_gt_1000)

print("\nRekordy, gdzie nadane imię jest takie jak Twoje:")
print(df_my_name)

print("\nSuma wszystkich urodzonych dzieci w całym danym okresie:", suma_urodzonych)

print("\nSuma dzieci urodzonych w latach 2000-2005:", suma_urodzonych_2000_2005)

print("\nSuma urodzonych chłopców:", suma_chlopcow)
print("Suma urodzonych dziewczynek:", suma_dziewczynek)

print("\nNajbardziej popularne imię dziewczynki i chłopca w danym roku:")
print(najpopularniejsze_imiona)

print("\nNajbardziej popularne imię dziewczynki i chłopca w całym danym okresie:")
print(najpopularniejsze_imiona_cały_okres)

#Zadanie 3
#Wczytaj plik /datasets/zamowienia.csv a następnie wyświetl:
# •listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# •5 najwyższych wartości zamówień
# •ilość zamówień złożonych przez każdego sprzedawcę
# •sumę zamówień dla każdego kraju
# •sumę zamówień dla roku 2005, dla sprzedawców z Polski
# •średnią kwotę zamówienia w 2004 roku,
# •zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv

print("Zadanie 3")


df1 = pd.read_csv('zamowienia.csv',header=0, sep=";",decimal='.')

print(df1.head())
df1['Data'] = pd.to_datetime(df1['Data zamowienia'])
df1['Rok'] = df1['Data'].dt.year

unikalne_nazwiska_sprzedawcow = df1['Sprzedawca'].unique()

najwyzsze_zamowienia = df1.nlargest(5, 'Utarg')

ilosc_zamowien_sprzedawcow = df1['Sprzedawca'].value_counts()

suma_zamowien_kraje = df1.groupby('Kraj')['Utarg'].sum()

suma_zamowien_polska_2005 = df1[(df1['Rok'] == 2005) & (df1['Kraj'] == 'Polska')]['Utarg'].sum()

srednia_kwota_2004 = df1[df1['Rok'] == 2004]['Utarg'].mean()

df1[df1['Rok'] == 2004].to_csv('zamowienia_2004.csv', index=False)

df1[df1['Rok'] == 2005].to_csv('zamowienia_2005.csv', index=False)

print("Lista unikalnych nazwisk sprzedawców:")
print(unikalne_nazwiska_sprzedawcow)

print("\n5 najwyższych wartości zamówień:")
print(najwyzsze_zamowienia)

print("\nIlość zamówień złożonych przez każdego sprzedawcę:")
print(ilosc_zamowien_sprzedawcow)

print("\nSuma zamówień dla każdego kraju:")
print(suma_zamowien_kraje)

print("\nSuma zamówień dla roku 2005, dla sprzedawców z Polski:")
print(suma_zamowien_polska_2005)

print("\nŚrednia kwota zamówienia w 2004 roku:")
print(srednia_kwota_2004)

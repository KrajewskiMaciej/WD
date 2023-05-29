# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from PIL import Image
#
# # plt.plot([1,3,5,7])
# # plt.show()
#
# # x=np.array([1,2,3,4])
# # y=x**2
# #
# # plt.plot(x,y,'ro-')
# # plt.axis([0,6,0,20])
# # plt.show()
# #
# # plt.plot(x,y,'r')
# # plt.plot(x,y,'o')
# # plt.axis([0,6,0,20])
# # plt.show()
#
# # x=np.arange(0,5,0.2)
# #
# # plt.plot(x,x,'r--',x,x**2,'bo',x,x**3,'g^')
# # plt.legend(labels=['liniowa','kwadratowa','sześcienna'])
# # plt.show()
# #
# # plt.plot(x,x,'r--',label='liniowa')
# # plt.plot(x,x**2,'bo',label='kwadratowa')
# # plt.plot(x,x**3,'g^',label='sześcienna')
# # plt.legend()
# # plt.show()
#
# # x=np.arange(0,10.1,0.1)
# # y=np.sin(x)
# #
# # plt.plot(x,y,'r--')
# # plt.xlabel('wartość X')
# # plt.ylabel('wartość sinx')
# # plt.legend()
# # plt.title('wykres liniowy funkcji sinx')
# # plt.show()
#
# # data={'a':np.arange(50),
# #       'c':np.random.randint(0,50,50),
# #       'd':np.random.randn(50)
# # }
# #
# # data['b']=data['a']+10*np.random.randn(50)
# # data['d']=np.abs(data['d'])*100
# #
# # plt.scatter('a','b',c='c',s='d',data=data,cmap='plasma')
# # plt.xlabel('klucz a')
# # plt.ylabel('klucz b')
# # plt.show()
#
# # x1=np.arange(0,2,0.02)
# # x2=np.arange(0,2,0.02)
# #
# # y1=np.sin(x1*np.pi*2)
# # y2=np.cos(x2*np.pi*2)
# #
# # plt.subplot(4,1,1)
# # plt.plot(x1,y1)
# # plt.title('wykres sin(x)')
# # plt.xlabel('x')
# # plt.ylabel('sin(x)')
# #
# # plt.subplots_adjust(hspace=0.5)
# #
# # plt.subplot(4,1,4)
# # plt.plot(x2,y2,'r')
# # plt.title('wykres cos(x)')
# # plt.xlabel('x')
# # plt.ylabel('cos(x)')
# # plt.show()
#
# # fig,axs=plt.subplots(3,2)
# # axs[0,0].plot(x1,y1)
# # axs[0,0].set_title('wykres sin(x)')
# # axs[0,0].set_xlabel('x')
# # axs[0,0].set_ylabel('sin(x)')
# #
# # axs[1,1].plot(x2,y2)
# # axs[1,1].set_title('wykres cos(x)')
# # axs[1,1].set_xlabel('x')
# # axs[1,1].set_ylabel('cos(x)')
# #
# # axs[2,0].plot(x1,y1,'r')
# # axs[2,0].set_title('wykres sin(x)')
# # axs[2,0].set_xlabel('x')
# # axs[2,0].set_ylabel('sin(x)')
# #
# # plt.subplots_adjust(hspace=0.5,wspace=0.5)
# #
# # fig.delaxes(axs[0,1])
# # fig.delaxes(axs[1,0])
# # fig.delaxes(axs[2,1])
# #
# # plt.show()
#
# # ts=pd.Series(np.random.randn(100))
# # ts=ts.cumsum()
# # plt.plot()
# # plt.show()
#
# # df=pd.read_csv('dane.csv',)
# #
# # grupa=df.groupby('Imię i Nazwisko').agg({'Wartość zamówienia':['sum']})
# # grupa.plot(kind='pie',subplots=True,)
#
#
# #24.05
#
# import seaborn as sns
#
# # ts=pd.Series(np.random.randn(1000))
# # ts=ts.cumsum()
# #
# # df=pd.DataFrame(ts, columns=['wartości'])
# # print(df)
# # df['średnia Krocząca']=df.rolling(window=50).mean()
# # df.plot()
# # plt.legend()
# # plt.show()
#
#
# # x=np.random.randn(1000)
# # plt.hist(x,bins=50,facecolor='g',alpha=0.75,density=True)
# # plt.xlabel('wartości')
# # plt.ylabel('Prawdopodobieństwo')
# # plt.title('Histogram')
# # plt.grid()
# # plt.show()
#
#
# df=pd.read_csv('dane.csv',header=0,sep=';',decimal='.')
# print(df)
# seria=df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
# wedges,texts,autotext=plt.pie(x=seria,labels=seria.index,
#                               autopct=lambda pct:"{:.1f}%".format(pct),
#                               textprops=dict(color="black"),
#                               colors=['red','green'])
# plt.title('Suma Zamówień dla sprzedawców')
# plt.legend(loc='lower right')
# plt.ylabel('Procentowy wynik wartości zamówienia')
# plt.show()

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

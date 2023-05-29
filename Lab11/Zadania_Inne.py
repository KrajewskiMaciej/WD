import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns

plt.plot([1,3,5,7])
plt.show()

x=np.array([1,2,3,4])
y=x**2

plt.plot(x,y,'ro-')
plt.axis([0,6,0,20])
plt.show()

plt.plot(x,y,'r')
plt.plot(x,y,'o')
plt.axis([0,6,0,20])
plt.show()

x=np.arange(0,5,0.2)

plt.plot(x,x,'r--',x,x**2,'bo',x,x**3,'g^')
plt.legend(labels=['liniowa','kwadratowa','sześcienna'])
plt.show()

plt.plot(x,x,'r--',label='liniowa')
plt.plot(x,x**2,'bo',label='kwadratowa')
plt.plot(x,x**3,'g^',label='sześcienna')
plt.legend()
plt.show()

x=np.arange(0,10.1,0.1)
y=np.sin(x)

plt.plot(x,y,'r--')
plt.xlabel('wartość X')
plt.ylabel('wartość sinx')
plt.legend()
plt.title('wykres liniowy funkcji sinx')
plt.show()

data={'a':np.arange(50),
      'c':np.random.randint(0,50,50),
      'd':np.random.randn(50)
}

data['b']=data['a']+10*np.random.randn(50)
data['d']=np.abs(data['d'])*100

plt.scatter('a','b',c='c',s='d',data=data,cmap='plasma')
plt.xlabel('klucz a')
plt.ylabel('klucz b')
plt.show()

x1=np.arange(0,2,0.02)
x2=np.arange(0,2,0.02)

y1=np.sin(x1*np.pi*2)
y2=np.cos(x2*np.pi*2)

plt.subplot(4,1,1)
plt.plot(x1,y1)
plt.title('wykres sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.subplots_adjust(hspace=0.5)

plt.subplot(4,1,4)
plt.plot(x2,y2,'r')
plt.title('wykres cos(x)')
plt.xlabel('x')
plt.ylabel('cos(x)')
plt.show()

fig,axs=plt.subplots(3,2)
axs[0,0].plot(x1,y1)
axs[0,0].set_title('wykres sin(x)')
axs[0,0].set_xlabel('x')
axs[0,0].set_ylabel('sin(x)')

axs[1,1].plot(x2,y2)
axs[1,1].set_title('wykres cos(x)')
axs[1,1].set_xlabel('x')
axs[1,1].set_ylabel('cos(x)')

axs[2,0].plot(x1,y1,'r')
axs[2,0].set_title('wykres sin(x)')
axs[2,0].set_xlabel('x')
axs[2,0].set_ylabel('sin(x)')

plt.subplots_adjust(hspace=0.5,wspace=0.5)

fig.delaxes(axs[0,1])
fig.delaxes(axs[1,0])
fig.delaxes(axs[2,1])

plt.show()

# 24.05


ts=pd.Series(np.random.randn(1000))
ts=ts.cumsum()

df=pd.DataFrame(ts, columns=['wartości'])
print(df)
df['średnia Krocząca']=df.rolling(window=50).mean()
df.plot()
plt.legend()
plt.show()


x=np.random.randn(1000)
plt.hist(x,bins=50,facecolor='g',alpha=0.75,density=True)
plt.xlabel('wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
plt.grid()
plt.show()


df=pd.read_csv('dane.csv',header=0,sep=';',decimal='.')
print(df)
seria=df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges,texts,autotext=plt.pie(x=seria,labels=seria.index,
                              autopct=lambda pct:"{:.1f}%".format(pct),
                              textprops=dict(color="black"),
                              colors=['red','green'])
plt.title('Suma Zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()

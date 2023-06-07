import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from PIL import Image

#Zadanie 1

x =np.arange(-5,8,0.1)

a=(np.sin(x)+(x**2))/np.cos(x**2)
plt.plot(x, a,'g--',label="f(x)=(sin(x)+x^2)/cos(x^2)")

plt.xlabel('x')
plt.ylabel('f(x)')

plt.axis([-4, 7, -400, 600])


plt.legend(loc='lower left')

plt.title('Wykres funkcji f(x) = cos(x)/x^2 dla x[-5,8]')

plt.show()

#Zadanie 2

x=np.arange(-4,4,0.01)

a=(5*(x**2))-(3*x)+2
b=(-2*(x**3)+5)

plt.subplot(2,3,2)

plt.plot(x,a,'r',label='5x^2*3x+2')
plt.xlabel("x")
plt.ylabel("Wynik funkcji")

plt.axis([-4, 4, 0, 100])

plt.title('Pierwszy wykres')
plt.legend(loc='upper right')

plt.subplot(2,3,4)

plt.plot(x,b,'g.',label='-2x^3+5')
plt.xlabel("x")
plt.ylabel("Wynik funkcji")

plt.axis([-4, 4, -100, 100])

plt.title('Drugi wykres')
plt.legend(loc='upper center')

plt.subplots_adjust(hspace=0.5,wspace=0.5)

plt.show()

#Zadanie 3

df = pd.read_csv('wine.data')

print(df)

randomowe = [np.random.randint(0, len(df)-1) for _ in range(100)]
df2 = df.iloc[randomowe]

print(df2)

grupy = df2.groupby('Class').size()

plt.pie(grupy, labels=grupy.index, autopct='%1.1f%%')
plt.legend()
plt.title("Udział klas")
plt.show()

#Zadanie 4

df1 = pd.read_csv('wine.data')
plt.show()

plot = sns.barplot(data=df1, x='Class', y='Alcohol',
                   errorbar=None, hue='Class', estimator=np.mean,
                   dodge=False, palette=['red', 'green', 'yellow'])
plot.legend(title='Klasa')
plot.set(title='Średnie Wartośći Alkoholu')

plt.show()


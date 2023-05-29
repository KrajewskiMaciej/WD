import math

#Zadanie 1

wynik= pow(((math.log(3,20))+(math.sin(45))*(5/8)),4)

print(round((wynik),2))
print("\n")

#Zadanie 2

lista=[2,6,12,3,37,7,10]

d=[lista[i] for i in range(0,len(lista)) if (i%2==0) & (lista[i]%2==0)]
nowa=d

print(lista)
print(nowa)
print("\n")

#Zadanie 3

list=[2, 5, 3.5, 2, 2, 6, 7, 8, 9,10,23,147]
list2=[]
a=len(list)
int(a)
if a%2==0:
    for i in range(0,int(a/2)):
        tmp=list[i]+list[len(list)-i-1]
        list2.append(tmp)
else:
    print("Nie ma listy wynikowej")

print(list,list2)
print("\n")

#Zadanie 4

tekst = open("tekst.txt",'r', encoding="utf-8")
tekst.read(48)
t=tekst.read(46)

duze=0
male=0
for i in range(0,len(t)):
    if t[i].isupper()==True:
        duze+=1

for i in range(0,len(t)):
    if t[i].islower()==True:
        male+=1


print(t)

if duze>0:
    print("Duże Litery:",duze)
else:
    print("Nie znaleziono dużych liter!")

if male>0:
    print("Małe Litery: ",male)
else:
    print("Nie znaleziono dużych liter!")
tekst.close()
print("\n")

#Zadanie 5

a=input("Podaj a:")
b=input("Podaj b:")
c=input("Podaj c:")

try:
    wynik=pow((int(a)/int(b)),3)*pow(int(c),(1/2))
    print("Wynik zapisano do pliku")
except:
    print("Błąd! Nie podano liczb!")

dane=open("zadanie5.txt","w+")
dane.writelines(str(wynik))

dane.close()
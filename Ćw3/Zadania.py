import math
#Zadanie 1
print((math.e)**10)

print(pow((math.log(5+math.sin(8)**2)),6))

print(math.floor(3.55))

print(math.ceil(4.80))

#Zadanie 2

imie='MACIEJ'
nazwisko="KRAJEWSKI"

imie=imie.lower()
nazwisko=nazwisko.lower()

print(imie.capitalize()+" "+nazwisko.capitalize())

#Zadanie 3

fragment='I to zabiera wdech Że obok jest ktoś i że Mogło być A jest wszystko A jest wszystko Jest wszystko Na na na na na Na na na na na Na na na na na Na na na na na'
szukane='na'
print(fragment.count(szukane, 0, len(fragment)))

#Zadanie 4

print(imie[1],imie[-1])

#Zadanie 5

string='Hello World'
print(string.split())

#Zadanie 6


float=2.1234125
hex='A1B23C'

print(string)
print(int(float))
print(int(hex,16))

#Zadanie 7

lista=['siatkowka','pilka nozna','koszykowka','pilka reczna','tennis','lekkoatletyka','skoki']

print(lista)
lista.reverse()
print(lista)
wiecej=['plywanie','slalom','wioslarstwo']
lista.extend(wiecej)
print(lista)

#Zadanie 8

slownik={'LoL':'Ligusia','CS:GO':'Przeciw Udezrenie: Globalna Ofensywa'}
print(slownik)

#Zadanie 9

ulubione_gry={'V':'Valorant','L':'Liga Legend','B3':'Borderlands 3','M':'Minecraft'}
print(len(ulubione_gry))

#Zadanie 10

zdanie=input("Podaj zdanie")

print(zdanie.count('a'))

#Zadanie 11

a=input("Podaj a: ")
b=input("Podaj b: ")
c=input("Podaj c: ")

a=int(a)
b=int(b)
c=int(c)

if a>b:
    if a>c:
        print("a Jest większe od b i c")
    else:
        print('a jest większe od b, ale mniejsze od c')
elif b>a:
    if b>c:
        print("b jest większe od a i c")
    else:
        print("b jest większe od a, ale mniejsze od c")

#Zadanie 12

liczby=[2,23,2.23475,12,279,7,2137]

for i in liczby:
    a=i**2
    print(a)

#Zadanie 13

parzyste=[]
i=0

while i<10:
    print("podaj liczbę ", i+1)
    z=input(" : ")
    z=int(z)
    if z%2==0:
        parzyste.append(z)
    i=i+1
print("Liczby Parzyste:",parzyste)

#Koniec listy

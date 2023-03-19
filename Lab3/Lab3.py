import math
import random
# #Obsługa Błędów
# print("Proszę podać pierwszą liczbę")
# licz1=input()
# print("Proszę podać drugą liczbę")
# licz2=input()
#
# try:
#     wynik=int(licz1)/int(licz2)
#     print("Wynik= "+str(wynik))
# except ZeroDivisionError:
#     print("Tylko Chuck Norris może dzielić przez zero!")
#
# #Python Compehension
# a = [x ** 2 for x in range(10)]
# b = [3 ** i for i in range(6)]
# c = [x for x in a if x % 2 == 1]
# print(a)
# print(b)
# print(c)
#
# skroty = {"PZU": "Państwowy zakład ubezpieczeń","ZUS": "Zaklad ubezpieczeń społecznych","PKO": "Państwowa kasa oszczędności"}
#
# odwrocone2 = {value: key for key, value in skroty.items()}
# print(odwrocone2,"\n")
#
#  #Funkcje
# def row_kwadratowe(a,b,c):
#     print("Obliczamy dla liczb: ",a,b,c)
#     delta = b**2 -4 * a *c
#     if delta < 0:
#         print("brak pierwiastków")
#         return -1
#     elif delta == 0:
#         print("jedne pierwiastek")
#         x = (-b) / (2 * a)
#         return x
#     else:
#         print("dwa pierwiaski")
#         x1 = (-b -math.sqrt(delta)) / (2 * a)
#         x2 = (-b + math.sqrt(delta)) / (2 * a)
#         return x1,x2
#
# print(row_kwadratowe(6,1,3))
# print("\n")
# print(row_kwadratowe(1,2,1))
# print("\n")
# print(row_kwadratowe(1,4,1))


#ZADANIA

#Zadanie 1

A = [1-x for x in range(1,11)]
B = [4**x for x in range(0,8)]
C = [x for x in B if x%2==0]

print(A)
print(B)
print(C)
print("\n")
#Zadanie 2

lista1=[random.randint(0,1000) for i in range(10)]
lista2=[x for x in lista1 if x%2==0]
print(lista1)
print(lista2)
print("\n")

#Zadanie 3

produkty={"marchewka":"szt",
          "ziemniaki":"kg",
          "truskawki":"kg",
          "jajka":"szt",
          "mleko":"szt"}
print(produkty)

prodSzt=[value for value, key in produkty.items() if key=="szt"]

print(prodSzt)

#Zadanie 4

def czyProstokatny(a,b,c):
    if (a**2)+(b**2)==(c**2):
        print("Trójkąt",a,",",b,",",c,"jest prostokątny")
        return "\n"
    else:
        print("Trójkąt",a,",",b,",",c,"nie jest prostokątny")
        return "\n"

print(czyProstokatny(3,4,5))
print(czyProstokatny(4,5,6))

#Zadanie 5

def poleTrapezu(a=3,b=4,h=5):
    pole=((a+b)*h)/2
    print("Pole Trapezu",a,",",b,",",h,":",pole)
    return "\n"

print(poleTrapezu(2,3,4))
print(poleTrapezu(7,95,2))
print(poleTrapezu())

#Zadanie 6

def iloczynElementow(a=1,b=4,ile=10):
    for i in range(0,ile):
        a*=b
    print("Wynik:",a)
    return "\n"

print(iloczynElementow())

#Zadanie 7

def iloczynEl(* z):
    il=1
    for i in z:
        il*=i
    print(il)

iloczynEl(3,5,7,9)

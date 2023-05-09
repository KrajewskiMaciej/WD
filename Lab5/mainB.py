

# Zad 1
# Dany jest plik tekst.txt. Dokonaj wczytania pliku wraz z obsługą polskich znaków oraz
# zapisz do zmiennej znaki, 40 znaków z tekstu zaczynając od 71 znaku tekstu.
# Następnie wyświetl tylko ilość litery „A” z wczytanego fragmentu, jeśli ich nie będzie wyświetl odpowiedni komunikat.

tekst = open("Tekst.txt",'r', encoding="utf-8")
tekst.read(70)
t=tekst.read(40)
a=t.count('a')
if(a==0):
    print("Brak 'a'")
else:
    print(a)
tekst.close()
# Zad 2
# Napisz skrypt, w którym utworzysz listę z liczbami,
# a następnie za pomocą python comprehension utwórz nową listę,
# która będzie zawierać tylko liczby zmiennoprzecinkowe, na koniec wyświetl obie listy.

list=[2,6,4.5,3,5.666,7,3.4]
outlist = []
for var in list:
    if var % 1 != 0:
        outlist.append(var)

print("Output List using for loop:", outlist)

# Zad 3
# Napisz funkcje, która jako argument przyjmuje listę z liczbami dowolnego typu.
# Zadaniem funkcji jest zrobienie sumy pierwszego elementu ze wszystkimi elementami z listy,
# dodanie ich na koniec do listy wejściowej i zwrócenie jej.

def doddaj(lista):
    wyjlista=lista
    for i in range(0, len(lista)):
        wyjlista.append(lista[1]+lista[i])
    return wyjlista

liste = [2,5,7]
print(doddaj(liste))

# Zad 4
# Napisz skrypt, który policzy i wyświetli wyrażenie.
# Wynik zaokrąglij do dwóch miejsc po przecinku.

import math

print(round(math.pow(math.sin(56),2)+math.pow(pow(4,2)/25+math.log(85,3),1/4),2))

# Zad 5
# Napisz skrypt, który pobiera od użytkownika konsoli liczbę całkowitą n, potem sumuje liczby od 1 do n.
# W skrypcie sprawdź błędy wczytanych typów wartości przy pomocy składni try/except.
# Na koniec wyświetl i zapisz wynik do pliku "Zadanie.txt".

try:
    n = int(input("Podaj n:"))

except:
    print("Błąd! Zły typ liczb!")

suma = sum(range(1, n+1))
plik = open("zadanie5.txt", "w",encoding="utf-8")
print(suma)
plik.writelines(str(suma))

plik.close()
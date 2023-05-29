
#Zadanie 1
# Za pomocą funkcji arange stwórz tablicę numpyskładającą się z 20 kolejnych wielokrotności liczby 4.
import numpy as np

a=np.arange(4, 4 * 21, 4)
print("Zadanie 1")
print(a)

#Zadanie 2
# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int32
lista=[1.2, 2.5, 3.7, 4.1, 5.9]

tablica = np.array(lista)

kopia = tablica.astype(np.int32)
print("Zadanie 2")
print(kopia)

#Zadanie 3
# Napisz funkcję, która będzie:
#   •Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
#   •Zwracała tablicę Numpy o wymiarach n*n kolejnych potęg liczby 2
def tablica_poteg(n):
    potegi = np.arange(n**2).reshape((n, n))
    return potegi

n = 5
wynik = tablica_poteg(n)
print("Zadanie 3")
print(wynik)

#Zadanie 4
# Napisz funkcję, która będzie przyjmowała 2 parametry:
# liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]

def generuj(p, i):
    potegi = np.power(p, np.arange(1,i+1))
    return potegi

# Przykład użycia funkcji
p = 2
i = 4
wynik = generuj(p, i)
print("Zadanie 4")
print(wynik)

#Zadanie 5
#Napisz funkcję, która:
#   •Na wejściu przyjmuje jeden parametr określający długość wektora
#   •Na podstawie parametru generuj wektor, ale w kolejności odwróconej
#   •Generuj macierz diagonalną z w/w wektorem na przekątnej oddalonej o 2 w górę od głównej przekątnej macierzy

def generuj_macierz(dlugosc):
    wektor = np.arange(dlugosc, 0, -1)

    macierz = np.diag(wektor, k=2)
    macierz=macierz[:dlugosc, :dlugosc]

    return macierz

dlugosc = 5
wynik = generuj_macierz(dlugosc)
print("Zadanie 5")
print(wynik)

#Zadanie 6
#Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.

def generuj_wykreslanke(slowo1, slowo2, slowo3):
    dlugosc_slowo1 = len(slowo1)+1
    dlugosc_slowo2 = len(slowo2)+1
    dlugosc_slowo3 = len(slowo3)
    dlugosc_max = max(dlugosc_slowo1, dlugosc_slowo2, dlugosc_slowo3)
    macierz = np.zeros((dlugosc_max, dlugosc_max), dtype='U1')

    for i, litera in enumerate(slowo1):
        macierz[i, 0] = litera

    for j, litera in enumerate(slowo2):
        macierz[dlugosc_max - 1, j] = litera

    slowo3_odwrocone = slowo3[::-1]
    for k, litera in enumerate(slowo3_odwrocone):
        macierz[k, k+1] = litera

    return macierz


slowo1 = "Wizualizacja"
slowo2 = "Danych"
slowo3 = "Python"
wynik = generuj_wykreslanke(slowo1, slowo2, slowo3)
print("Zadanie 6")
print(wynik)

#Zadanie 7
#Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
# [4 2 4]
# [6 4 2]]
# Przy założeniach:
# funkcja przyjmuje parametr n,
# który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2
# na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.

def generuj_macierz(n):
    macierz = np.zeros((n, n), dtype=int)

    for i in range(n):
        for j in range(n):
            if i == j:
                macierz[i, j] = 2
            elif i == (j + 1) or i == (j - 1):
                macierz[i, j] = 2 * (abs(i - j) + 1)
            else:
                macierz[i, j] = 2 * (abs(i - j) + 1)

    return macierz

n = 3
wynik = generuj_macierz(n)
print("Zadanie 7")
print(wynik)

#Zadanie 8
#Napisz funkcję, która:
# •jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# •parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# •funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość wierszy lub kolumn,
# w zależności od kierunku podziału, nie pozwala na operację)

def podziel_tablice(tablica, kierunek):
    if kierunek == 'pionowo':
        if tablica.shape[0] % 2 != 0:
            print("Nie można podzielić tablicy na pół w pionie. Ilość wierszy nie pozwala na operację.")
            return None

        polowa = tablica.shape[0] // 2
        tablica1 = tablica[:polowa, :]
        tablica2 = tablica[polowa:, :]

        return tablica1, tablica2
    elif kierunek == 'poziomo':
        if tablica.shape[1] % 2 != 0:
            print("Nie można podzielić tablicy na pół w poziomie. Ilość kolumn nie pozwala na operację.")
            return None

        polowa = tablica.shape[1] // 2
        tablica1 = tablica[:, :polowa]
        tablica2 = tablica[:, polowa:]

        return tablica1, tablica2
    else:
        print("Nieprawidłowy kierunek. Dostępne opcje: 'pionowo', 'poziomo'.")
        return None


# Przykład użycia funkcji
tablica = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
kierunek = 'poziomo'
wynik = podziel_tablice(tablica, kierunek)
print("Zadanie 8")
if wynik:
    print("Tablica 1:")
    print(wynik[0])
    print("Tablica 2:")
    print(wynik[1])


#Zadanie 9
#Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy
# i stwórz macierz 5x5, która będzie zawierała kolejne wartości ciągu arytmetycznego.

start = 1
krok = 2
rozmiar = 5

koniec = start + (rozmiar * rozmiar - 1) * krok
macierz = np.arange(start, koniec + 1, krok).reshape((rozmiar, rozmiar))
print("Zadanie 9")
print(macierz)

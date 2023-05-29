

#Zadanie 1
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.

import numpy as np

macierz1 = np.array([2, 4, 6])
macierz2 = np.array([1, 3, 5])

wynik = macierz1 * macierz2
print("Zadanei 1")
print(wynik)

#Zadanie 2
#Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

print("Zadanie 2")

macierz_3x3 = np.array([[9, 2, 5],
                        [1, 7, 3],
                        [4, 6, 8]])

min_k_3x3 = np.amin(macierz_3x3, axis=0)
print("Najniższe wartości dla każdej kolumny w macierzy 3x3:")
print(min_k_3x3)

min_w_3x3 = np.amin(macierz_3x3, axis=1)
print("Najniższe wartości dla każdego wiersza w macierzy 3x3:")
print(min_w_3x3)

macierz_4x4 = np.array([[7, 5, 2, 9],
                        [3, 1, 8, 4],
                        [6, 2, 4, 7],
                        [9, 3, 1, 5]])

min_k_4x4 = np.amin(macierz_4x4, axis=0)
print("Najniższe wartości dla każdej kolumny w macierzy 4x4:")
print(min_k_4x4)

min_w_4x4 = np.amin(macierz_4x4, axis=1)
print("Najniższe wartości dla każdego wiersza w macierzy 4x4:")
print(min_w_4x4)

#Zadanie 3
#Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.


iloczyn = np.dot(macierz1, macierz2)
print("Zadanie 3")
print(iloczyn)

#Zadanie 4
#Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste.
# Następnie wykonaj na nich operację mnożenia.

macierz4_1 = np.array([1, 2, 3], dtype=int)
macierz4_2 = np.array([1.5, 2.5, 3.5], dtype=float)


wynik4= np.multiply(macierz4_1, macierz4_2)

print("Zadanie 4")
print(wynik4)

#Zadanie 5
#Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości i zapisz do zmiennej “a”.

macierz = np.array([[1, 2, 3], [4, 5, 6]])

a = np.sin(macierz)
print("Zadanei 5")
print("Macierz:")
print(macierz)
print("Sinusy:")
print(a)

#Zadanie 6
#Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej wartości i zapisz do zmiennej “b”.
print("Zadanei 6")

macierz6 = np.array([[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]])

b = np.cos(macierz6)

print("Macierz:")
print(macierz6)
print("Cosinusy:")
print(b)

#Zadanie 7
#Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.
print("Zadanie 7")

wynik7 = a + b

print("Macierz a (sinusy):")
print(a)
print("Macierz b (cosinusy):")
print(b)
print("Wynik dodawania:")
print(wynik7)

#Zadanie 8
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.
print("Zadanie 8")

macierz8 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

for row in macierz8:
    print(row)

#Zadanie 9
#Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy.
# (użyj funkcji flat())

print("Zadanie 9")

macierz9 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

for element in macierz9.flat:
    print(element)

#Zadanie 10
#Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?

print("Zadanie 10")
macierz10 = np.arange(1, 82).reshape(9, 9)

new_shape1 = macierz10.reshape(3, 27)

new_shape2 = macierz10.reshape(27, 3)

new_shape3 = macierz10.reshape(1, 81)

print("Macierz 3x27:")
print(new_shape1)
print("Macierz 27x3:")
print(new_shape2)
print("Macierz 1x81:")
print(new_shape3)

#Po wygenerowaniu macierzy 9x9, mamy różne możliwości zmiany jej kształtu
# (czyli zmiany liczby wierszy i kolumn) w zależności od wymagań i potrzeb naszego zadania.
# Oto kilka możliwości zmiany kształtu macierzy 9x9:
#1. Zamiana na macierz 3x27:
#    Możemy zmienić kształt macierzy 9x9 na 3x27, gdzie każdy wiersz macierzy 9x9 staje się wierszem macierzy 3x27.
#    W tej konfiguracji, każdy wiersz macierzy 3x27 będzie zawierał oryginalne elementy jednego wiersza macierzy 9x9.
# 2. Zamiana na macierz 27x3:
#    Możemy również zmienić kształt macierzy 9x9 na 27x3,
#    gdzie każdy kolumna macierzy 9x9 staje się kolumną macierzy 27x3.
#    W tej konfiguracji, każda kolumna macierzy 27x3 będzie zawierać oryginalne elementy jednej kolumny macierzy 9x9.
# 3. Zamiana na macierz 1x81:
#    Inną możliwością jest zmiana kształtu macierzy 9x9 na macierz 1x81. W tej konfiguracji,
#    wszystkie elementy macierzy 9x9 są łączone w jednym wierszu macierzy 1x81.
# 4. Zamiana na macierz 18x4 lub 36x2:
#    Możemy także zmienić macierz 9x9 na macierz 18x4 lub 36x2, podzielając macierz na mniejsze bloki.
# Dlaczego mamy te różne możliwości zmiany kształtu? Dzieje się tak, ponieważ liczba elementów w macierzy
# (w tym przypadku 9x9 = 81) pozostaje taka sama, niezależnie od kształtu.
# Możemy manipulować kształtem macierzy w celu dostosowania jej do wymagań obliczeniowych,
# analizy danych lub innych operacji, które są bardziej efektywne lub łatwiejsze do wykonania na macierzy o określonym kształcie.

#Zadanie 11
#Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki.

print("Zadanie 11")

vector = np.arange(1, 13)

macierz_3x4 = vector.reshape(3, 4)

macierz_4x3 = vector.reshape(4, 3)

macierz_2x6 = vector.reshape(2, 6)

print("Macierz 3x4:")
print(macierz_3x4)
print("Spłaszczona macierz 3x4:")
print(macierz_3x4.flatten())

print("Macierz 4x3:")
print(macierz_4x3)
print("Spłaszczona macierz 4x3:")
print(macierz_4x3.flatten())

print("Macierz 2x6:")
print(macierz_2x6)
print("Spłaszczona macierz 2x6:")
print(macierz_2x6.flatten())
#Zad. 3 Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

with open("Zadanie 3.txt","w+") as plik:
    for i in range(15):
        plik.write("Ludzie zawsze będą gadać,\n")


otworz=open("Zadanie 3.txt","r")
linia=otworz.readlines()
otworz.close()

print(linia)
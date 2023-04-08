
zadanaLiczba = int(input("Podaj liczbę do sprawdzenia: "))

if zadanaLiczba == 1:
    print("Liczba nie jest pierwsza")
    exit()

for i in range(2, zadanaLiczba):
    if zadanaLiczba%i == 0:
        print("Liczba jest złożona")
        exit()

print("Liczba jest pierwsza")
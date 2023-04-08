end = None

def silnia(x):
    wynik = 1
    for i in range(1, x+1):
        wynik *= i
    end
    return wynik
end

E = 0

for i in range(0,10):
    E += 1/silnia(i)
end

print("Wartosc e wynosi: " + str(E))

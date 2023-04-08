end = None

x = float(input("Podaj kąt x dla cosx: ")) # np. cos(0.523333) = 0.866 wartosci podane okolo

def silnia(n):
    temp = 1
    for i in range(1, (n)+1):
        temp *= i
    end
    return temp
end

wynik = 1

for n in range(1, 10):
    wynik += (((-1)**n)/silnia(2*n))*(x**(2*n))
end

print(wynik)
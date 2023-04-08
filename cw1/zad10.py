import math
end = None

# Pierwszy algorytm(wolny)
def sumaDzielnikow(x):
    suma = 0
    i = 1
    while i <= math.sqrt(x):
        if x % i == 0:
            suma += i
            suma += int(x/i);
        i += 1
    suma -= x
    return suma
    end
end

print("Liczby doskonale do miliona to: ") # 6, 28, 496, 8128

for i in range(2,1000001):
    if sumaDzielnikow(i) == i:
        print(i, end=", ")
end

print("Koniec")
"""
# ========================================
# Drugi algorytm szybki
# sito + metoda euklidesa na liczby parzyste doskonałe
sito = []

for i in range(0, 1000001):
    sito.append(1)
end
    
sito[0] = 0
sito[1] = 0

for i in range(2, 1000):
    if sito[i] == 1:
        j = i*i
        while j<1000001:
            sito[j] = 0
            j += i
        end
    end
end

print("Liczby doskonale do miliona to: ")
i = 1
j = 1
while j*i < 1000001:
    if sito[j]:
        k = j * i
        print(k, end=", ")
    end
    i *= 2
    j += i
end
"""
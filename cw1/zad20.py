from math import sqrt
end = None
epsilon = 0.00001

def nextA(a, b):
    return sqrt(a*b)
end

def nextB(a, b):
    return (a+b)/2
end

liczba1 = int(input("Podaj pierwsza liczbe: "))
liczba2 = int(input("Podaj druga liczbe: "))

geo = nextA(liczba1, liczba2)
art = nextB(liczba1, liczba2)

while abs(geo-art) > epsilon:
    tempA = geo
    tempB = art
    geo = nextA(tempA, tempB)
    art = nextB(tempA, tempB)
end

print("Srednia arytmetyczno-geometryczna liczb wynosi: ")
print(geo)
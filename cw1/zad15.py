from math import sqrt
end = None

s = sqrt(0.5)
wynik = sqrt(0.5)

for i in range(1, 100):
    s = sqrt(0.5 + (0.5*s))
    wynik *= s
end

wynik = 2/wynik

print(wynik)
import math
end = None

k = int(input("Podaj liczbę: "))

print("Podzielniki liczby to: ", end="")

i = 1

while i < math.sqrt(k):
    if k%i == 0:
        print(i, end=", ")
        print(int(k/i), end=", ")
    end
    i += 1
end


"""
for i in range(1, k+1):
    if k%i == 0:
        print(i, end=", ")
"""



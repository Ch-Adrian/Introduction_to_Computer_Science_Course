end = None
from math import sqrt

N = int(input("Podaj liczbę naturalną: "))

sq = sqrt(N)
i = int(sq)
while i>0:
    if N%i==0:
        print("Dwie liczby to: ", str(i), 'i', str(N//i))
        break
    end
    i -= 1
end
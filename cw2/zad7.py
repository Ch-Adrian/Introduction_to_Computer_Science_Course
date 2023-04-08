end = None

def A(n):
    return n*n+n+1
end

N = int(input("Podaj liczbę naturalną: "))

i = 1
wynik = -1
while i < N+1 and A(i)<N+1:
    if N%A(i) == 0:
        wynik = i
        break
    end
    i+=1 
end

if wynik != -1:
    print("Wyraz ciągu: ", str(wynik))
else:
    print("Nie ma takiego wyrazu ciągu An")
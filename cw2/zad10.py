end = None

def A(n):
    a = 2
    for j in range(1, n+1):
        a = 3*a + 1
    end
    return a
end

N = int(input("Podaj liczbę naturalną: "))

a = 2
while a<=N:
    if N%a == 0:
        print("Liczba jest wielokrotnością: ", a)
        break
    end
    a = 3*a + 1
    if a>N:
        print("Liczba nie jest wielokrotnością")
    end
end
end = None

N = int(input("Podaj liczbę N: "))

def silnia(a):
    w = 1
    for i in range(1, a+1):
        w *= i
    end
    return w
end

wynik = []
ulamek = []

for i in range(0, N+1):
    wynik.append(0)
    ulamek.append(0)
end


for i in range(2, 10):
    
    a = 1
    b = silnia(i)
    j = 0
    while j<N:
        a *= 10
        ulamek[j] = a//b
        a = a%b
        j += 1
    end
    for k in range(0, N+1):
        wynik[k] += ulamek[k]
        ulamek[k] = 0
    end
end

for i in range(N, 0, -1):
    a = wynik[i]%10
    wynik[i-1] += wynik[i]//10
    wynik[i] = a
end

print("2.", end="")
for i in wynik:
    print(i, end="")
    
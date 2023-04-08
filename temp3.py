end = None

def S(n,k):
    if n==k: return 1
    if n==0: return 0
    return S(n-1, k-1) + k*S(n-1, k)
end

def silnia(n):
    a = 1
    for i in range(n+1):
        a *= i
    end
    return a
end

def liczbaPodzialow():
    a = silnia(n)
    while True:
        b = int(input("Podaj przez co dzielic(gdy -1 koniec): "))
        if b == -1: break
        a /= silnia(b)
    end
    return a
end

n = int(input("Podaj n>> "))
k = int(input("Podaj k>> "))
a = int(input("Podaj a[0 to S(n,k), 1 to podzial]: "))

if a == 0:
    print(S(n,k))
elif a == 1:
    print(liczbaPodzialow())
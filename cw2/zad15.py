end = None

def liczbaNcyfrowa(n):
    dl = len(str(n))
    a = n
    suma = 0
    while a>0:
        suma += (a%10)**dl
        a//=10
    end
    if n == suma:
        return True
    else:
        return False
    end
end

N = int(input("Podaj N: "))

liczba1 = 1
while len(str(liczba1)) != N: liczba1*=10

for i in range(liczba1, liczba1*10):
    if liczbaNcyfrowa(i):
        print(i)
    end
end

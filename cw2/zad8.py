end = None

N = int(input("Podaj N: "))

def sprawdz(n):
    if n == 1 or n == 2:
        return True
    end
    
    pocz1 = 1
    pocz2 = 0
    kon1 = 1
    kon2 = 0
    suma = 0
    while suma <= n and pocz1 <= n:
        suma += pocz1
        temp  = pocz1
        pocz1 = pocz1 + pocz2
        pocz2 = temp
        if suma > n:
            while suma>n:
                suma -= kon1
                t = kon1
                kon1 = kon1 + kon2
                kon2 = t
            end
        end
        if suma == n:
            # print(kon1,", ", pocz2)
            return True
        end
    end
    if pocz1 > n:
        return False
end


i = N+1
while sprawdz(i): i += 1
print(i)
end = None

def rozne(a,b):
    while a>0:
        a1 = a%10
        b1 = b
        while b1>0:
            if b1%10 == a1:
                return False
            end
            b1 //= 10
        end
        a //= 10
    end
    return True
end

def innaPodstawa(n, podstawa):
    wynik = ""
    while n > 0:
        wynik += str(n%podstawa)
        n = n//podstawa
    end
    return int(wynik)
end
    

liczba1 = int(input("Podaj pierwszą liczbę: "))
liczba2 = int(input("Podaj drugą liczbę: "))

for i in range(2, 17):
    if rozne(innaPodstawa(liczba1, i), innaPodstawa(liczba2, i)):
        print("Znaleziona podstawa to: ", i)
        break
    end
    if i == 16:
        print("Nie ma takiej podstawy")
    end
end
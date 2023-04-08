import math as m
end = None

n = int(input("Podaj liczbę naturalną: "))
system = int(input("Podaj system(2 - 16): "))

def liczbaIpodstawa(n, system):
    wynik = []
    while n > 0:
        wynik.append(n%system)
        n = n//system
    end
    return wynik
end

def liczipods(n, system):
    liczby = "0123456789ABCDEF"
    wynik = [0]*(int(m.log(n,2)+1))
    i = 0
    while n>0:
        wynik[i] = liczby[n%system]
        n//=system
        i+=1
    end
    wynik.reverse()
    print(wynik)
    i = 0
    for i in range(len(wynik)):
        if wynik[i]!=0: break
    end
    return wynik[i:]
end


#wynik.reverse()
print(liczipods(n, system))

"""
funkcja NWD(a,b) - zwraca największy wspólny dzielnik a i b
funkcja NWD_1(a,b,c) - zwraca True jeśli największy wspólny
dzielnik a,b,c to 1

Funkcja trojki składa się z 4 pętli, poszczególne pętle szukają wzorca:
1    liczba, liczba, liczba
2    liczba, liczba,  _ , liczba
3    liczba, _ , liczba, liczba
4    liczba, _ , liczba , _ , liczba
gdzie liczba to interesująca nas liczba do trojki, a liczba pod _ nie jest
brana do trojki
"""
end = None

def NWD(a,b):
    while b != 0:
        a , b = b , a%b
    end
    return a
end

def NWD_1(a,b,c):
    if NWD(a,b) == 1 and NWD(a,c) == 1 and NWD(b,c) == 1:
        return True
    else: return False
end

def trojki(T):
    N = len(T)
    counter = 0
    
    for i in range(2, N):
        if NWD_1(T[i], T[i-1], T[i-2]):
            counter += 1
        end
    end
    
    for i in range(3, N):
        if NWD_1(T[i],T[i-2], T[i-3]):
            counter += 1
        end
    end
    
    for i in range(3, N):
        if NWD_1(T[i], T[i-1], T[i-3]):
            counter += 1
        end
    end
    
    for i in range(4, N):
        if NWD_1(T[i], T[i-2], T[i-4]):
            counter += 1
        end
    end
    
    return counter
end
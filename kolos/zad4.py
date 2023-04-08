"""
Funkcja rekurencyjna wywołuje trzy razy siebie.
Gdy obecnie jest liczba pierwsza to:
    Tworzy nową liczbę  albo
    dodaje kolejną cyfrę do obecnej liczby.
albo
    dodaje kolejną cyfrę do obecnej liczby.

ale gdy np nie mamy liczby pierwszej to nie tworzy kolejnyej liczby.
"""
end = None

def divide(N):
    def lp(a):
        if a== 2 or a== 3 or a == 5: return True
        if a<2 or not a%2 or not a%3 or not a%5: return False
        
        b = 5
        while b*b<=a:
            b+=2
            if not a%b: return False
            b+=4
            if not a%b: return False
        end
        return True
    end
    
    def rek(N, newN=0, p=0, lpodz = 1):
        if N == 0:
            if lp(newN) and lp(lpodz):
                return True
        elif lp(newN):
            if rek(N//10, N%10, 1, lpodz+1): return True
            if rek(N//10, (10**p)*(N%10)+newN, p+1, lpodz): return True
        else:
            if rek(N//10, (10**p)*(N%10)+newN, p+1, lpodz): return True
        end
        return False
    end
    
    return rek(N)
end

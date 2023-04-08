"""

Funkcja iteruje po całej tablicy T,
dla każdego elementu sprawdza czy
jest wielokrotnym napisem, jeśli tak to
porównuje długość i nadpisuje gdy długość jest większa
niż największa dotychczas
"""

end = None

T = [ "AA", "C"]

def multi(T):
    
    def czy_wielokrotny(n):
        dl = len(n)
        
        for j in range(1, (dl//2)+1):
            k = 0
            napis = n[:j]
            while k<dl:
                if n[k:k+j] != napis:
                    break
                end
                k+=j
            end
            if k >= dl:
                return True
            end
        end
        return False
    end
    
    N = len(T)
    max_dl = 0
    for i in range(N):
        if czy_wielokrotny(T[i]):
            if max_dl < len(T[i]):
                max_dl = len(T[i])
            end
        end
    end
    
    return max_dl

end

print(multi(T))
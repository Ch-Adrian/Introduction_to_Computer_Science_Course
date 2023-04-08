end = None
from random import randint

def lpierwsza(a):
    if a==2 or a == 3: return True
    if a<2 or not a%2 or not a%3: return False
    
    b = 5
    while b*b<=a:
        b+=2
        if not a%b: return False
        b+=4
        if not a%b: return False
    end
    
    return True
end

def komp(T):
    
    N = len(T)
    # i to wiersze
    for i in range(N):
        # j to kolumny
        for j in range(N):
            if T[i][j] == 0: continue
            znaleziona = False
            #dla tego samego wiersza k to kolumny
            for k in range(j+1, N):
                if T[i][k] != 0:
                    if lpierwsza(T[i][j]+T[i][k]):
                        print(i,j,i,k)
                        T[i][j] = 0
                        T[i][k] = 0
                        znaleziona = True
                        break
                    end
                end
            end
            
            if znaleziona:
                continue
            
            # kolejne wiersze, gdzie k to wiersze
            for k in range(i+1, N):
                for l in range(N):
                    if T[k][l] != 0:
                        if lpierwsza(T[i][j]+T[i][k]):
                            print(i,j,k,l)
                            T[i][j] = T[k][l] = 0
                            znaleziona = True
                            break
                        end
                    end
                end
                if znaleziona:
                    break
            end
            if znaleziona:
                continue
        end
    end
end
        
N = 10
T = [ [ randint(1, 10) for _ in range(10)] for _ in range(10) ]

for i in range(N):
    for j in range(N):
        print(T[i][j], end=" ")
    end
    print()
end

komp(T)

for i in range(N):
    for j in range(N):
        print(T[i][j], end=" ")
    end
    print()
end

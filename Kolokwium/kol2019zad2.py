end = None

t = [ [1,1,1,1,1], [1,1,1,1,1], [1,0,1,1,0], [1,1,1,1,1], [1,1,1,1,1] ]

def niepJed(t):
    N=len(t)
    #maksymalnie mogą być 2 liczby o parzystej liczbie jedynek
    T2 = [ (-1,-1) , (-1,-1) ]
    wskT2 = 0
    
    #czy t[i][j] ma nieparzysta liczbe jedynek
    for i in range(N):
        for j in range(N):
            temp = t[i][j]
            ileJed = 0
            while temp>0:
                if temp%2:
                    ileJed += 1
                end
                temp //= 2
            end
            
            if not ileJed%2:
                if wskT2<2:
                    T2[wskT2] = i,j
                    wskT2 += 1
                else:
                    return False
                end
            end
        end
    end

    # sprawdzamy czy znaleziono jakąkolwiek liczbę o parzystej ilości jedynek
    if wskT2 == 0:
        return True
    else:
        if T2[0][0] != T2[1][0]: return False
    end
    
    return True
end
        
print(niepJed(t))             
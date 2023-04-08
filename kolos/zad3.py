"""
Program zlicza w tablicach pomocniczych sumy poszczególnych elementów
w kolumnach i wierszach. Następnie wyszukuje odpowiednio pola pierwszego
i drugiego w tablicy. Sprawdza czy to nie to samo pole. Wylicza
sumę szachowanych pól i porównuje czy jest największa.
"""
end = None

def chess(T):
    N = len(T)
    # Tw[w] to suma liczb w wierszu w
    # Tk[k] to suma liczb w kolumnie k
    Tw = [0]*N
    Tk = [0]*N
    
    for w in range(N):
        for k in range(N):
            Tw[w] += T[w][k]
            Tk[k] += T[w][k]
        end
    end
    
    maxSum = 0
    pos = ((-1,-1),(-1,-1))
    
    # wyszukujemy pozycji (i,j) i (x,y), gdzie x!=i i y!=j
    for i in range(N):
        for j in range(N):
            for x in range(N):
                for y in range(N):
                    if y != j and x != i:
                        tmp = Tw[i] + Tk[j]-2*T[i][j] \
                            + Tw[x] + Tk[y] - 2*T[x][y] \
                            -T[x][j]-T[i][y]
                        if maxSum<tmp:
                            maxSum = tmp
                            pos = (i,j,x,y)
                        end
                    end
                end
            end
        end
    end
    
    return pos                        
end

end = None

def tower(T):
    N = len(T)

    Tw = [0]*N
    Tk = [0]*N
    sumField = 0
    for w in range(N):
        for k in range(N):
            Tw[w]+= T[w][k]
            Tk[k]+= T[w][k]
        end
    end

    print(Tw)
    print(Tk)
    wynik = ((-1,-1),(-1,-1))
    for i in range(N):
        for j in range(N):
            for x in range(N):
                if x != i:
                    for y in range(N):
                        if y != j:
                            tmp = Tw[i]-T[i][j]+Tk[j]-T[i][j] \
                                    + Tw[x]-T[x][y]+Tk[y]-T[x][y]-T[i][y]-T[x][j]
                            if tmp > sumField:
                                sumField = tmp
                                wynik = ((i,j), (x,y))
                            end
                        end
                    end
                end
            end
        end
    end

    return wynik
end

T = [[1,2,1,3],[1,2,1,3],[1,2,1,3],[1,2,1,3]]

print(tower(T))




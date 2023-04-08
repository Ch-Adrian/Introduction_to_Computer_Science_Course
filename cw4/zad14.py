end = None

def bin(a):
    counter = 0
    while a>0:
        if a%2: counter += 1
        a//=2
    end
    return counter
end

def compa(T1, T2):
    N1 = len(T1)
    N2 = len(T2)
    prc33 = int(0.33*N1*N1)
    print("prc33: ", prc33)

    for i in range(N1):
        for j in range(N1):
            T1[i][j] = bin(T1[i][j])
        end
    end
    
    for i in range(N2):
        for j in range(N2):
            T2[i][j] = bin(T2[i][j])
        end
    end
    
    print(T1)
    print(T2)

    for i in range(N2-N1+1):
        for j in range(N2-N1+1):

            compatib = 0
            for x in range(N1):
                for y in range(N1):
                    if T1[x][y] == T2[x+i][y+j]: compatib+=1
                end
            end

            if compatib > prc33: return True
        end
    end

    return False
end

T1 = [[3,3],[3,3]]
T2 = [[1,1,1],[1,3,1],[1,1,3]]

print(compa(T1,T2))

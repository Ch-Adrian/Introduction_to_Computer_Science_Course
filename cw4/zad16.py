end = None

def wlp(T):
    def lpierwDo10(a):
        if a==2 or a==3 or a==5 or a==7: return True
    end

    def cyfpierw(a):
        
        while a>0:
            if lpierwDo10(a%10):
                return True
            a//=10
        end
        return False
    end

    N = len(T)

    counter = 0
    for i in range(N):
        for j in range(N):
            if cyfpierw(T[i][j]):
                counter += 1
                break
            end
        end
    end

    if counter == N: return True
    return False
end

T = [[0,1,1,1],[1,3,1,1],[1,1,1,3],[1,1,3,1]]

print(wlp(T))

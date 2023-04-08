end = None
from random import randint

T = [ [randint(1,10) for _ in range(10)] for _ in range(10)]

for i in range(10):
    T[5][i] = 0
    T[i][5] = 0

for i in range(10):
    for j in range(10):
        print(T[i][j], end=" ")
    end
    print()
end

def fzero(T):
    N = len(T)
    Trz = [False for _ in range(N)]
    
    for i in range(N):
        j = 0
        while j<N and T[j][i] != 0: j+=1
        if j<N and T[j][i] == 0:
            Trz[j] = True
        else:
            return False
        end
    end
    
    for i in range(N):
        if not Trz[i]:
            j=0
            while j<N and T[i][j] != 0: j+=1
            if j==N:
                return False
            end
        end
    end
    return True
end

print(fzero(T))

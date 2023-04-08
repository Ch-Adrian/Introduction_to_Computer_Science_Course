end = None
from random import randint

# do testu ////////////////
N = 6
T = [ [ randint(1, 10) for _ in range(N)] for _ in range(N)]

T[1][1] = 10
T[1][5] = 10
T[5][1] = 10
T[5][5] = 10

for i in range(N):
    for j in range(N):
        print(T[i][j], end=" ")
    end
    print()
end
#////////////////////////

def fsquare(T, k):
    N = len(T)

    for i in range(3, N, 2):
        for rz in range(N-i+1):
            for kol in range(N-i+1):
                if (T[rz][kol] * T[rz][kol+i-1] * T[rz+i-1][kol] * T[rz+i-1][kol+i-1]) == k:
                    return (True, (rz, kol))
                end
            end
        end
    end
    return (False, (None, None))
end

print(fsquare(T, 10000))
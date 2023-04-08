end = None
from random import randint

N = 5
T = [ [randint(1, 100) for _ in range(N)] for _ in range(N)]

T[3][3] = 1
T[3][2] = 1
T[2][3] = 1
T[4][3] = 1
T[3][4] = 1

for i in range(N):
    for j in range(N):
        print(T[i][j], end=" ")
    end
    print()
end

def areFriends(a,b):
    tab = [ False for _ in range(10)]
    while a>0:
        tab[a%10] = True
        a//=10
    end
    while b>0:
        if not tab[b%10]:
            return False
        end
        b //= 10
    end
    return True
end

def friends(T):
    N = len(T)
    counter = 0
    
    for rz in range(N):
        for kol in range(N):
            strony = 0
            ile_stron = 0
            if kol>=0 and rz>0:
                ile_stron += 1
                if areFriends(T[rz][kol], T[rz-1][kol]):
                    strony += 1
                end
            end
            if kol>0 and rz>=0:
                ile_stron += 1
                if areFriends(T[rz][kol], T[rz][kol-1]):
                    strony += 1
                end
            end
            if kol<N and rz<N-1:
                ile_stron += 1
                if areFriends(T[rz][kol], T[rz+1][kol]):
                    strony += 1
                end
            end
            if kol<N-1 and rz<N:
                ile_stron += 1
                if areFriends(T[rz][kol], T[rz][kol+1]):
                    strony += 1
                end
            end
            if strony == ile_stron:
                counter += 1
            end
        end
    end
    return counter
end

print(friends(T))
                
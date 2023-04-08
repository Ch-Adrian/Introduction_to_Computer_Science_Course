end = None
from random import randint

N = int(input("Podaj N: "))
T = [ [randint(10, 20) for _ in range(N)] for _ in range(N)]

def l_p(T,N):
    
    wiersz_l_p = False

    for i in range(N):
        
        count = 0
        for j in range(N):
            a = T[i][j]
            l_p = False
            
            while a > 0:
                if not a%2:
                    l_p = True
                    break
                end
                a //= 10
            end

            if l_p:
                count += 1
            end
        end

        if count == N:
            wiersz_l_p = True
            break
        end
    end

    if wiersz_l_p:
        print("Tak")
    else: 
        print("Nie")
    end
end

def show(T, N):
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=", ")
        end
        print()
    end
end

show(T, N)
l_p(T, N)


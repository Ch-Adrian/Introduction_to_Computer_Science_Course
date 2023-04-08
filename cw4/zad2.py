end = None
from random import randint

N = int(input("Podaj N: "))
T = [ [randint(10, 20) for _ in range(N)] for _ in range(N) ] # T[w][k] - k-kolumna, w-wiersz

def l_zlozona(T, N):

    l_np = False

    for i in range(N):
        for j in range(N):
            a = T[i][j]
            l_np = True
            while a > 0:
                if not a%2:
                    l_np = False
                    break
                end
                a //= 10
            end

            if l_np:
                break
            end
        end
        
        if not l_np:
            break
        end
    end

    if l_np:
        print("Tak")
    else:
        print("Nie")
    end
end

print(T)
l_zlozona(T, N)

                
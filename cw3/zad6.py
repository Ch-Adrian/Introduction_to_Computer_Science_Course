end = None

from random import randint

N = int(input("Podaj wartość N: "))

t = [0 for _ in range(N)]


for i in range(N):
    t[i] = randint(1, 1000)
end
#print(t)

for i in range(N):
    jest_np = False
    #print(tab[i])
    a = t[i]
    while a > 0:
        if a%2:
            jest_np = True
            break
        end
        a //= 10
    end
    #print(jest_np)
    if not jest_np:
        break
    end
end

if jest_np:
    print("Każdy element zawiera cyfrę nieparzystą")
else:
    print("Nie każdy element zawiera cyfrę nieparzystą")


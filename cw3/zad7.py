end = None

from random import randint

N = int(input("Podaj wartość N: "))

t = [0 for _ in range(N)]


for i in range(N):
    t[i] = randint(1, 1000)
end
#print(t)

for i in range(N):
    jest_np = True
    #print(tab[i])
    a = t[i]
    while a > 0:
        if not a%2:
            jest_np = False
            break
        end
        a //= 10
    end
    #print(jest_np)
    if jest_np:
        break
    end
end

if jest_np:
    print("Istnieje element zawierający same nieparzyste cyfry")
else:
    print("Nie istnieje element zawierający same nieparzyste cyfry")
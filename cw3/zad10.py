end = None
from random import randint

def spa(t, N):
    dl = 0
    for i in range(N-1):
        r = t[i+1] - t[i]
        j = i
        counter = 0
        while j< N-1 and r == t[j+1] - t[j]:
            counter += 1
            if dl < counter:
                dl = counter
            end
            j += 1
        end
    end
    print(dl + 1) # dl to ilość par o tej samej różnicy, jest ich o jeden mniej niż samych liczb w ciągu
end

N = int(input("Podaj długość tablicy: "))
t = [ 0 for _ in range(N) ]

for i in range(N):
     t[i] = int(input(">> "))
    #t[i] = randint(1, 100)
end

# print(t)
spa(t,N)

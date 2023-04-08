end = None
from random import randint

def spg(t, N):
    dl = 0
    for i in range(N-1):
        q = t[i+1] / t[i]
        j = i
        counter = 0
        while j< N-1 and q == t[j+1] / t[j]:
            counter += 1
            if dl < counter:
                dl = counter
            end
            j += 1
        end
    end
    print(dl + 1) # dl to ilość par o tej samej wielokrotności, jest ich o jeden mniej niż samych liczb w ciągu
end

N = int(input("Podaj długość tablicy: "))
t = [ 0 for _ in range(N) ]

for i in range(N):
     t[i] = int(input(">> "))
    #t[i] = randint(1, 100)
end

# print(t)
spg(t,N)


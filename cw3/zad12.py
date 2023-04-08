end = None
from random import randrange

def spa(t, N, czy_dod):
    dl = 0
    #if not czy_dod: t.reverse()
    
    for i in range(N-1):
        r = t[i+1] - t[i]
        if not r: continue
        if ((r<0) == czy_dod): continue
        #if r<=0: continue
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
    #if not czy_dod: t.reverse()
    return(dl + 1) # dl to ilość par o tej samej różnicy, jest ich o jeden mniej niż samych liczb w ciągu
end

N = int(input("Długość tablicy: "))

t = [randrange(1, 99, 2) for _ in range(N)]

#print(t)
print(spa(t, N, True), spa(t, N, False))
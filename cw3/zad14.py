end = None
from random import randint

for N in range(20, 41):
    counter = 0
    for _ in range(100):
        t = [ randint(1, 365) for _ in range(N)]
        find = False
        for i in range(N):
            for j in range(N-1, i, -1):
                if t[i] == t[j]:
                    counter += 1
                    find = True
                    break
                end
            end
            if find: break
        end
    end
    print("Dla ", N, ": ", counter/100)
end
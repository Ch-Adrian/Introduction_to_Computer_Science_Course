end = None
from random import randint

N = int(input("Podaj N: "))
t = [ int(input(">>> ") ) for _ in range(N) ]
max_r = 0
print(t)

for i in range(N):
    
    j = N-1
    while j>=0:
        while j>=0 and t[i] != t[j]:
            j -= 1
        end
        a = i
        b = j
        r = 0
        while a<N and b >= 0 and t[a] == t[b]:
            r += 1
            a += 1
            b -= 1
        end
        if max_r<r:
            max_r = r
        end
        j -= 1
    end
end

print(max_r)
    
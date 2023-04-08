end = None
from random import randint

def spn(t, N):
    a = t[0]
    t[0] = 1
    for i in range(N-1):
        if t[i+1] > a:
            a = t[i+1]
            t[i+1] = t[i] + 1
        else:
            a = t[i+1]
            t[i+1] = 1
        end
    end
    # print(t)
    print("Długość najdłuższego spójnego podciągu wynosi: ",max(t))
end

N = int(input("Podaj długość tablicy: "))
t = [ 0 for _ in range(N) ]

for i in range(N):
    # t[i] = int(input(">> "))
    t[i] = randint(1, 100)
end

# print(t)
spn(t,N)
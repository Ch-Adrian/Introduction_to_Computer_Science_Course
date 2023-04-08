end = None

N = int(input("Podaj liczbę N: "))

sito = []
for i in range(0, N+1):
    sito.append(1)
end

sito[0] = 0
sito[1] = 0

i = 2
while i*i < N:
    if sito[i] == 1:
        for j in range(i*i, N+1, i):
            sito[j] = 0
        end
    end
    i += 1
end

for i in range(2, N):
    if sito[i] == 1:
        print(i, end=", ")
    end
end

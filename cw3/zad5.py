end = None

tablica = []
temp = int(input())

while temp != 0:
    tablica.append(temp)
    temp = int(input())
end

"""Rozwiązanie #1"""
tablica2 = sorted(tablica)
a = 1
for i in range(1, len(tablica2)):
    if tablica2[i-1] != tablica2[i]:
        a+=1
    end
    if a == 10:
        print("10 co do wielkości wartość to: ", tablica2[i])
    end
end



"""Rozwiązanie #2
for licznik in range(1, 11):
    j = 0
    a=tablica[0]
    while a == -1 and j < len(tablica):
        j+=1
        a = tablica[j]
    end

    for i in range(0, len(tablica)):
        if tablica[i] != -1 and tablica[i] < a:
            a = tablica[i]
        end
    end

    for i in range(0, len(tablica)):
        if tablica[i] == a:
            tablica[i] = -1
        end
    end
    if licznik == 10:
        print("10 co do wielkości wartość to: ", str(a))
    end
end
"""

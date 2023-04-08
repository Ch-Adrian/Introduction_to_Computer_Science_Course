end = None

n1 = int(input("Podaj pierwszą liczbę: "))
n2 = int(input("Podaj drugą liczbę: "))

tablica = []

while n1>0:
    tablica.append(n1%10)
    n1 //= 10
end
dl = 0
while n2>0:
    temp = n2%10
    for i in range(0, len(tablica)):
        if temp == tablica[i]:
            tablica[i] = -1
        end
    end
    n2 //= 10
    dl +=1
end

bezCyfr= True
for i in tablica:
    if i != -1:
        bezCyfr = False
    end
end

if dl == len(tablica) and bezCyfr:
    print("Liczby mają te same cyfry")
else:
    print("Liczby nie mają tych samych cyfr")
end
            
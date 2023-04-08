end = None

n = int(input("Podaj liczbę naturalną: "))

arrFibb = []

def genFibbTo(a):
    f1 = 1
    f2 = 1
    while f1 <= a:
        arrFibb.append(f1)
        temp = f1
        f1 = f1 + f2
        f2 = temp
    end
end

genFibbTo(n)

for i in range(0, len(arrFibb)):
    for j in range(i+1, len(arrFibb)):
        if arrFibb[i] * arrFibb[j] == n:
            print('Liczba ', n, ' jest iloczynem dwóch liczb fibbonacciego: ')
            print(arrFibb[i])
            print(arrFibb[j])
            exit(0)
        elif arrFibb[i] * arrFibb[j] >= n: break
        end
    end
end

print('Liczba nie jest iloczynem dwóch liczb fibbonacciego')
            
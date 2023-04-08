end = None

N = int(input("Podaj liczbę naturalną: "))

w=N%10
while N>0:
    N//=10
    m = N%10
    if w<=m:
        print("Cyfry nie mają ciągu rosnącego")
        break
    end
    w = m
    N //= 10
    if N == 0:
        print("Cyfry mają ciąg rosnący")
    end
end
    
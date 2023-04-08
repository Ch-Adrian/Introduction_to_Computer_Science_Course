end = None

N = int(input("Podaj liczbę naturalną: "))

a = N%10
N//=10
while N>0:
    b = N%10
    if a==b:
        print("Ostatnia cyfra nie jest unikalna")
        break
    end
    N //= 10
    if N==0:
        print("Ostatnia cyfra jest unikalna")
    end
end
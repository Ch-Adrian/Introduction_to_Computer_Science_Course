end = None

N = input("Podaj liczbę naturalną: ")

licznik = len(N)
N = int(N)

while N>0:
    a = N%10
    if a == licznik:
        break
    end
    N //= 10
end

if a == licznik:
    print("Liczba zawiera cyfrę równą liczbie swoich cyfr")
else:
    print("Liczba nie zawiera cyfry równej liczbie swoich cyfr")
end
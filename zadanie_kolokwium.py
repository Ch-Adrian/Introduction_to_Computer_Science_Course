end = None

N = int(input("Proszę podać N>> "))

wynik = 1
for i in range(1, N+1):
    wynik *= i
    while not wynik%10:
        wynik /= 10
    end
    wynik %= 1000000
end

print(int(wynik%10))
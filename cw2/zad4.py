end = None

n = int(input("Podaj liczbę: "))

def ileLiczb(m):
    ile = 0
    for i in range(1, m+1):
        a = i
        while a%2 == 0:
            a/=2
        end

        while a%3 == 0:
            a/=3
        end

        while a%5 == 0:
            a/=5
        end

        if a == 1:
            ile+=1
        end
    end
    return ile
end

print("Liczb dwu-trzy-piątkowych jest: ", ileLiczb(n))

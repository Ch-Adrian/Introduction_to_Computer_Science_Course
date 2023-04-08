end = None

def podzial(n):
    def rek(n, t, pos=0):
        if n == 0:
            for i in range(pos):
                print(t[i], end=" ")
            end
            print()
        end

        for i in range(n, 0, -1):
            if n-i >= 0:
                if pos == 0 or i <= t[pos-1]:
                    t[pos] = i
                    rek(n-i, t, pos+1)
            end
        end
    end

    t = [0 for _ in range(n) ]
    rek(n, t)
end

podzial(10)

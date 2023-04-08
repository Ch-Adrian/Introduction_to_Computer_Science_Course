end = None

def zad1(l):
    def lpierwsza(a):
        if a == 2 or a == 3 or a == 5: return True
        if a<2 or not a%2 or not a%3 or not a%5: return False

        b = 5
        while b*b<=a:
            b+=2
            if not a%b: return False
            b+= 4
            if not a%b: return False
        end
        return True
    end

    def rek(l, l2=0, p=0, zm=False):
        if l == 0 and l2>9 and lpierwsza(l2) and zm:
            print(l2)
        elif l!= 0:
            rek(l//10, (10**p)*(l%10)+l2, p+1, True)
            rek(l//10, l2, p, zm)
        end
    end

    rek(l)
end

zad1(1234)

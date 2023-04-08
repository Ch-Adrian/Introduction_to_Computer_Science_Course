end = None

def dziel(x):
    def lpierwsza(a):
        if a == 2 or a == 3 or a == 5: return True
        if a<=2 or not a%2 or not a%3 or not a%5: return False
    
        b = 5
        while b*b<=a:
            b+=2
            if not a%b: return False
            b+=4
            if not a%b: return False
        end
        return True
    end
    
    def rek(x, sett):
        # liczymy długość liczby
        dl = 0
        temp = x
        while temp>0:
            dl+=1
            temp//=10
        end

        if dl<2: return None
        if lpierwsza(x): sett.add(x)
        
        m=1
        dz = 10
        for i in range(dl):
            a = x%m
            b = x//dz
            rek(b*m+a, sett)
            m*=10
            dz*=10
        end
    end
    
    sett=set()
    rek(x,sett)
    print(sett)
        
end

dziel(14523)
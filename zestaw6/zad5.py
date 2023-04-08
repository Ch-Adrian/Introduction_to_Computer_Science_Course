end = None

U = [1,1,1,0,1,1]
T = [1,1,0,1,0,0]

def ciag(T):
    def lpierwsza(a):
        if a==2 or a== 3 or a == 5: return True
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
    
    def pierwBin(T, a, b):
        # T[a]T[a+1]...T[b] - liczba 
        if a==b: return False
        dl = b-a+1
        l = 0
        for i in range(dl):
            if T[b-i]: l += 2**i
        end
        return lpierwsza(l)
    end
    
    def cut(T, ost):
        i = 1
        while i <= 30:
            if ost+i >= len(T): break
            if pierwBin(T, ost+1, ost+i):
                if ost+i==len(T)-1: return True
                elif cut(T, ost+i): return True
            end
            i += 1
        end
        return False
    end
    
    return cut(T, -1)
end

print(ciag(U))
print(ciag(T))
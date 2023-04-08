end = None

def wlp(T):
    
    def lpierwsza(a):
        if a==2 or a==3 or a==5: return True
        if a<2 or not a%2 or not a%3 or not a%5: return False

        b = 5
        while b*b<=a:
            b+=2
            if not a%b: return False
            b+=4
            if not a%b: return False
        end
        return True
    end

    def cyfpier(a):

        while a>0:
            if lpierwsza(a%10): return True
            a//=10
        end
        return False
    end

    N = len(T)
    
    for w in range(N):
        counter = 0
        for k in range(N):
            if cyfpier(T[w][k]):
                counter += 1
            else: break
        end
        if counter == N: return True
    end
    
    return False
end

T = [[1,1,1,1],[15,15,15,15],[13,13,13,1],[1,1,1,1]]
    
print(wlp(T))

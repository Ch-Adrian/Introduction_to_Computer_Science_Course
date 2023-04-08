end = None

T = [[1,1,2],[2,1,1],[1,2,1]]

def zad21(T, val):
    Tk = [ True for _ in range(len(T)) ]

    def rek(T, val, nval = 0, w = 0):
        if nval == val: return True
        N = len(T)
        for k in range(N):
            if Tk[k] and w<N:
                Tk[k]=False
                if rek(T, val, nval+T[w][k], w+1): 
                    print(w, k)
                    return True
                Tk[k]=True
            end
        end
        return False
    end

    return rek(T,val)
end

print(zad21(T,6))

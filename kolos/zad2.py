"""

"""

end = None

T = [ [1,1,1], [1,1,0], [0,0,1]]

def distance(T):
    # gdy a-b<0 zwraca watrość [-1] inaczej tablicę z liczbą
    def roznica(a,b):
        N = len(a)
        
        p = [0 for _ in range(N)]
        # odejmujemy dwie liczby
        for i in range(N-1, -1, -1):
            p[i] = a[i]-b[i]
        end
        for i in range(N-1, -1, -1):
            if p[i]<0:
                j = i-1
                while j>=0 and p[j] != 1:
                    p[j] -= 1
                    p[j+1] += 2 
                    j -= 1
                end
                if j == -1:
                    return [-1 for _ in range(N)]
                else:
                    p[j] -= 1
                    p[j+1] += 2
                end
        end
        
        return p
    end
    
    # porównuje a>b, gdy tak to 1 inaczej -1
    def czy_mniejsza(a,b):
        N =len(a)
        for i in range(N):
            if a[i] != b[i]:
                if a[i]:
                    return 1
                else:
                    return -1
                end
            end
        end
    end
    
    N = len(T)
    p = [ 0 for _ in range(N)]
    odl = 0
    for i in range(N):
        for j in range(i+1, N):
            w = roznica(T[i],T[j])
            if p<w:
                odl = j-i
                for k in range(N):
                    p[k] = w[k]
                end
            end
        end
    end
    
    return odl
end

print(distance(T))
end = None

T = [ 2, 2, 2, 3, 3, 4, 5, 1, 76]

def podZb(T):
    # liczy podzbiory jako sumy elementow
    def waga(x):
        w = 0
        temp = 2
        while x>1:
            if not x%temp:
                w+=1
                while not x%temp:
                    x//=temp
                end
            end
            temp+=1
        end
        return w
    end

    def findPodZb(T, n, a, b, c):
        # funkcja zwraca krotkę (True/False, a, b, c)
        if n+1<len(T):
            tmp1 = findPodZb(T, n+1, a+T[n+1], b, c)
            tmp2 = findPodZb(T, n+1, a, b+T[n+1], c)
            tmp3 = findPodZb(T, n+1, a, b, c+T[n+1])
            if tmp1[0]:
                return tmp1
            elif tmp2[0]:
                return tmp2
            elif tmp3[0]:
                return tmp3
            else:
                return (False, 0, 0, 0)
        else:
            w = waga(b)
            if waga(a)==w and w == waga(c): return (True, a, b, c)
            else: return (False, 0, 0, 0)
        end
    end
    k = findPodZb(T, -1, 0, 0, 0)
    print(k)
    
    return k[0]
end

def podZbW(T):
    # liczy podzbiory jako sumy wag elementow
    def waga(x):
        w = 0
        temp = 2
        while x>1:
            if not x%temp:
                w+=1
                while not x%temp:
                    x//=temp
                end
            end
            temp+=1
        end
        return w
    end

    def findPodZb(T, n, a, b, c):
        # funkcja zwraca krotkę (True/False, a, b, c)
        if n+1<len(T):
            w = waga(T[n+1])
            tmp1 = findPodZb(T, n+1, a+w, b, c)
            tmp2 = findPodZb(T, n+1, a, b+w, c)
            tmp3 = findPodZb(T, n+1, a, b, c+w)
            if tmp1[0]:
                #print((a+w,b,c))
                return tmp1
            elif tmp2[0]:
                #print((a,b+w,c))
                return tmp2
            elif tmp3[0]:
                #print((a,b,c+w))
                return tmp3
            else:
                return (False, 0)
        else:
            if a==b and b == c: return (True, a)
            else: return (False, 0)
        end
    end
    k = findPodZb(T, -1, 0, 0, 0)
    print(k)
    
    return k[0]
end

print(podZb(T))
print(podZbW(T))
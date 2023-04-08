end = None

t=[ [ 2 for _ in range(8)] for _ in range(8) ]

t[1][2] = 1
t[2][1] = 1
t[3][0] = 1
t[4][1] = 1
t[5][2] = 1
t[6][3] = 1
t[7][4] = 1

def king(t, k):
    def findWay(t, w, k, cost):
        if w+1<=7:
            a = c = -1
            if k-1>=0: a = findWay(t, w+1, k-1, cost+t[w+1][k-1])
            b = findWay(t, w+1,  k, cost+t[w+1][k])
            if k+1<=7: c = findWay(t, w+1, k+1, cost+t[w+1][k+1])
            if a == -1: a=b
            if c==-1: c=b
            return min(a,b,c)
        else: return cost
    end
    
    return findWay(t, 0, k, t[0][k])
end

print(king(t, 2))
            
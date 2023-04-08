end = None

N = 5
T = [[0 for _ in range(N)] for _ in range(N) ]

# tablica wypelniona zerami
def horse(T):
    def fillArr(T, n, a, b):
        if T[a][b] == 0:
            N = len(T)-1 # czyli N to ostatni indeks
            T[a][b] = n
            if a+1<=N and b+2<=N:
                if fillArr(T, n+1, a+1, b+2): return True
            if a+2<=N and b+1<=N:
                if fillArr(T, n+1, a+2, b+1): return True
            if a+1<=N and b-2>=0:
                if fillArr(T, n+1, a+1, b-2): return True
            if a+2<=N and b-1>=0:
                if fillArr(T, n+1, a+2, b-1): return True
            if a-1>=0 and b-2>=0:
                if fillArr(T, n+1, a-1, b-2): return True
            if a-2>=0 and b-1>=0:
                if fillArr(T, n+1, a-2, b-1): return True
            if a-2>=0 and b+1<=N:
                if fillArr(T, n+1, a-2, b+1): return True
            if a-1>=0 and b+2<=N:
                if fillArr(T, n+1, a-1, b+2): return True
            T[a][b] = 0
            return False
        else:
            if n-1 == (len(T)**2):
                return True
            else: return False
        
    end
    
    fillArr(T, 1, 0, 0)
    N = len(T)
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=" ")
        print()
end

horse(T)
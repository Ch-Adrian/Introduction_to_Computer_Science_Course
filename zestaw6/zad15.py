end = None

N = 8
T = [ [ 0 for _ in range(N)] for _ in range(N)]

def H(T, n):
    Tk = [ True for _ in range(n)]
    T1 = [ True for _ in range(2*n-1)]
    T2 = [ True for _ in range(2*n-1)]
    def hetman(T, n, w=0):
        if w == 8: return True
        for i in range(n):
            k = i
            if (Tk[i] and T1[w+i] and T2[w-i+n-1]):
                    T[w][i] = 1
                    Tk[i] = T1[w+k] = T2[w-k+n-1] = False
                    if hetman(T, n, w+1): return True
                    Tk[i] = T1[w+k] = T2[w-k+n-1] = True
            end
            T[w][i] = 0
        end
    end
    hetman(T, n)
end

H(T, N)
for i in range(N):
	for j in range(N):
		print(T[i][j], end=" ")
	end
	print()
end

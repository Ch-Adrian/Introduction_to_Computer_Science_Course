end = None

def Hanoi(n):
	if n == 1: return 1
	return 2*Hanoi(n-1) + 1
end

def HanoiRoz(n):

	def show(n, a,b,c):
		print(a)
		print(b)
		print(c)
		print()
	end

	def rek(N, a, idxA, b, idxB, c, idxC):
		if N > 0:
			idxA, idxC, idxB = rek(N-1, a, idxA, c, idxC, b, idxB)
			show(N, a,b,c)
			c[idxC] = a[idxA-1]
			a[idxA-1] = 0
			idxC+=1
			idxA-=1
			idxB, idxA, idxC = rek(N-1, b, idxB, a, idxA, c, idxC)
			return idxA, idxB, idxC
		return idxA, idxB, idxC

	end

	a = [ i for i in range(n, 0, -1)]
	b = [ 0 for _ in range(n)]
	c = [ 0 for _ in range(n)]
	rek(n, a, n, b, 0, c, 0)
	show(n, a,b,c)
end

HanoiRoz(3)
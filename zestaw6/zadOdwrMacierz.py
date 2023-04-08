end = None

T = [[1,0,0,1],[0,0,2,1],[0,1,1,1],[2,1,1,2]]
D = [[2,-3,-1],[1,-1,0],[2,0,1]]
E = [[2,5,0], [-1,-3,0], [0,4,2]]

# z tw. Laplace'a
def odw(M):
	def det(M):
		if len(M) == 2:
			return M[0][0]* M[1][1] - M[0][1]*M[1][0]
		end
		a = 0
		for i in range(len(M)):
			a += M[0][i]*compl(M,0,i)
		end
		return a
	end

	def minor(M, w,k):
		tmp = [ [0 for _ in range(len(M)-1)] for _ in range(len(M)-1)]
		a = b = 0
		for i in range(len(M)):
			if i == w: continue
			for j in range(len(M)):
				if j == k: continue
				tmp[a][b] = M[i][j]
				b+=1
			end
			b=0
			a+=1
		end

		return det(tmp)
	end

	def compl(M, w, k):
		return ((-1)**(w+k))*minor(M,w,k)
	end

	def odwStart(M):

		N = len(M)
		A = [ [ 0 for _ in range(N)] for _ in range(N)]
		# Macierz dopełnień
		for i in range(N):
			for j in range(N):
				A[i][j] = compl(M, i, j)
			end
		end
		# Macierz transponowana
		for i in range(N):
			for j in range(i, N):
				A[j][i], A[i][j] = A[i][j], A[j][i]
			end
		end

		tmp = (det(M)**(-1))
		for i in range(N):
			for j in range(N):
				A[i][j] *= tmp
			end
		end

		return A
	end


	if det(M) != 0:
		return odwStart(M)
	end
end

A = odw([[73,-28.5,57],[-52.5,20.5,-41],[20,-10,28]])

for i in range(len(A)):
	for j in range(len(A)):
		print(A[i][j], end=" ")
	end
	print()
end
end = None

T = [ [0, 2, -3], [1, -2, 4], [-1, 3, -4] ] # -3
N = [[2,7,-1,3,2], [0,0,1,0,1], [-2,0,7,0,2], [-3,-2,4,5,3], [1,0,0,0,1] ]# 123
M = [[1,0,1,-1], [2,1,-1,2], [-1,2,1,3], [3,-1,4,0]]
A = [[1,-1,2], [2,1,3], [-1,4,0]]
B = [[2,1,2], [-1,2,3], [3,-1,0]]
C = [[2,1,-1], [-1,2,1], [3,-1,4]]

# z tw. Laplace'a
def det(M):
	def countDet(M):
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

		return countDet(tmp)
	end

	def compl(M, w, k):
		return ((-1)**(w+k))*minor(M,w,k)
	end

	return countDet(M)

end

print(det([[73,-28.5,57],[-52.5,20.5,-41],[20,-10,28]]))
print(det(A))
print(det(B))
print(det(C))
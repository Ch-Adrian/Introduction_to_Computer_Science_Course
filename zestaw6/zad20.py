end = None

N= 8
T = [ [i for i in range(N)] for _ in range(N)]

#T[0][1] = 0
#T[1][2] = 0
#T[2][3] = 0
#T[3][4] = 0
#T[4][5] = 0
#T[5][6] = 0
#T[6][7] = 0
#T[7][1] = 0

def odl(w, k, nw,nk, wdoc, kdoc):
	if abs(w-wdoc)>= abs(nw-wdoc) and abs(k-kdoc)>= abs(nk-kdoc):
		return True
	end
	return False
end

#kierunki
# 0 1 2
# 3 x 4
# 5 6 7

def krol(T,  w= 0, k =0, wDoc = 7, kDoc = 7, wsk = 0):
	if w == wDoc and k == kDoc:
		return True, [0 for i in range(20)]

	wek = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	for i in range(8):
		nw = wek[i][0]+w
		nk = wek[i][1]+k
		if odl(w, k, nw, nk, wDoc, kDoc) and T[w][k]%10 < T[nw][nk]//(10**(len(str(T[nw][nk]))-1)):
			tmp = krol(T, nw, nk, wDoc, kDoc, wsk+1)
			if tmp[0]:
				tmp[1][wsk] = i 
				return True, tmp[1]
		end
	end
	return False, 0
end

print(krol(T, 0, 0, 7, 7)[1])


end = None

N= 8
T = [ [i for i in range(N)] for _ in range(N)]

T[0][1] = 0
T[1][2] = 0
T[2][3] = 0
T[3][4] = 0
T[4][5] = 0
T[5][6] = 0
T[6][7] = 0
T[7][1] = 0

def odl(w, k, nw,nk, wdoc, kdoc):
	if abs(w-wdoc)>= abs(nw-wdoc) and abs(k-kdoc)>= abs(nk-kdoc):
		return True
	end
	return False
end

def krol(T, w= 0, k =0, wDoc = 7, kDoc = 7):
	if w == wDoc and k == kDoc:
		return True
	wek = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
	for i in wek:
		nw = i[0]+w
		nk = i[1]+k
		if odl(w, k, nw, nk, wDoc, kDoc) and T[w][k]%10 < T[nw][nk]//(10**(len(str(T[nw][nk]))-1)):
			if krol(T, nw, nk, wDoc, kDoc): return True
		end
	end
	return False
end

print(krol(T))


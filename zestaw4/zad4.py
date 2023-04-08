end = None
import zad1

T = [ (1,1), (1,7), (1,2), (1,4), (8,1), (13,1), (16,1), (24,1)]

def spojne(T):
	LA = 0
	LG = 0
	N = len(T)

	# zliczamy LA
	i = 0
	while i< N-2:

		if zad1.odejmij(T[i], T[i+1]) == zad1.odejmij(T[i+1], T[i+2]):
			j = i
			dl = 0
			
			while j < N - 2 and zad1.odejmij(T[j], T[j+1]) == zad1.odejmij(T[j+1], T[j+2]): 
				j += 1
				dl += 1
			end

			dl += 2
			#jeśli nie zliczamy podciągow
			i = j
			LA += 1
		end
		i += 1
	end

	# zliczamy LG
	i = 0
	while i < N-2:

		#print(("i", i, i+1, i+2))
		#print(zad1.podziel(T[i], T[i+1]))
		if zad1.podziel(T[i], T[i+1]) == zad1.podziel(T[i+1], T[i+2]):
			j = i
			dl = 0

			while j < N - 2 and zad1.podziel(T[j], T[j+1]) == zad1.podziel(T[j+1], T[j+2]): 
				j += 1
				dl += 1
			end

			dl += 2
			#jeśli nie zliczamy podciągow
			i = j
			LG += 1
		end
		i += 1
	end
	#print(LA, LG)
	if LA > LG: return 1
	elif LA < LG: return -1
	else: return 0

end

def niespojne(T):
	
	N = len(T)

	LA = 0
	LG = 0

	for i in range(N):
		for j in range(i+1, N):
			for k in range(j+1, N):
				if zad1.odejmij(T[i], T[j]) == zad1.odejmij(T[j], T[k]):
					print("LA", i,j,k)
					LA += 1
				end
				if zad1.podziel(T[i], T[j]) == zad1.podziel(T[j], T[k]):
					print("LG", i,j,k)
					LG += 1
				end
			end
		end
	end

	if LA > LG: return 1
	elif LA < LG: return -1
	else: return 0

end

print(niespojne(T))
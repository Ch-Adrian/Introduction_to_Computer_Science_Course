end = None
from random import randint
T = [ (randint(0, 99), randint(0,99)) for _ in range(10) ]

for i in T:
	print(i)
end

def szach(dane):

	N = len(dane)

	for i in range(N):
		for j in range(i+1, N):
			w1, k1 = dane[i]
			w2, k2 = dane[j]
			if w1 == w2 or k1 == k2 or w1-k1 == w2-k2 or w1+k1 == w2+k2:
				print("Dwa hetmany maja szach: ")
				print(dane[i], dane[j])
				return False
			end
		end
	end
	print("Hetmany nie maja szacha")
	return True
end

print(szach(T))
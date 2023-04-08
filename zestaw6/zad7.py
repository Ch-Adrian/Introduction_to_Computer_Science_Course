end = None

T= [ 1, 3, 5, 10, 16, 24 ]

def odw(T, m):
	def spr(T, m, counter = 0):
		if m == 0: return True
		if counter >= len(T): return False
		return spr(T, m - T[counter], counter+1) or spr(T, m, counter+1)
	end

	return spr(T, m)
end

print(odw(T, 21))
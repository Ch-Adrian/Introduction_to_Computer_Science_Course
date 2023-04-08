end = None

def liczba(a,b):
	def lpierwsza(c):
		if c== 2 or c == 3 or c == 5: return True
		if c<2 or not c%2 or not c%3 or not c%5: return False

		d = 5
		while d*d<=c:
			d+=2
			if not c%d: return False
			d+=4
			if not c%d: return False
		end

		return True
	end

	def rek(a, b, dl, c=0, p=0):
		#print("c=",c, " p=", p,a,b)
		if p==dl and lpierwsza(c):
			print(c)
			return 1
		else:
			d = e = 0
			if a != 0:
				d = rek(a//10, b , dl,(10**(p))*(a%10)+c, p+1)
			if b != 0:
				e = rek(a, b//10 , dl , (10**(p))*(b%10)+c, p+1)
			return d + e
		end
		return 0
	end

	dl = len(str(a)) + len(str(b))
	return rek(a, b, dl)
end

print(liczba(13, 75))
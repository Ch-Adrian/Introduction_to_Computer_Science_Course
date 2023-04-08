end = None

def wyraz(s1, s2):
	def waga(a):
		suma = 0
		samog = 0
		for i in a:
			if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'y':
				samog += 1
			end
			suma += ord(i)
		end
		return (suma, samog)
	end

	def rek(wS1,S2, dlS2, nowyS2, wsk):
		if wS1 == waga(nowyS2):
			return (True, nowyS2)
		if wsk<dlS2:
			# nie dodajemy literki
			a = rek(wS1, S2, dlS2, nowyS2, wsk+1)
			# dodajemy literke
			b = rek(wS1, S2, dlS2, nowyS2+S2[wsk], wsk+1)
			if a[0]: return a
			if b[0]: return b
		end
		return (False, "")
	end

	wynik = rek(waga(s1), s2, len(str(s2)), "", 0)
	if wynik[0]:
		print(wynik[1])
		return True
	else: return False

end

wyraz("exe", "uglba")
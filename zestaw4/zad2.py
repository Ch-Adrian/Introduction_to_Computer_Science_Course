end = None
import zad1

def rrown(a,b,c,d,e,f):
	"""
	ax+by = c
	dx+ey = f

	y = (c - ax)/b
	x = (f-ey)/d

	y = (c - a[(f-ey)/d])/b
	x = (f-e[(c - a[(f-ey)/d])/b])/d
	"""
	a = a,1
	b = b,1
	c = c,1
	d = d,1
	e = e,1
	f = f,1
	"""
	print(zad1.pomnoz(e,a))
	print(zad1.pomnoz(b,d))
	print(zad1.pomnoz(a,f))
	print(zad1.pomnoz(d,c))
	print(zad1.odejmij(zad1.pomnoz(b,d), zad1.pomnoz(e,a)))
	print(zad1.odejmij(zad1.pomnoz(d,c), zad1.pomnoz(a,f)))
	print(zad1.podziel(zad1.odejmij(zad1.pomnoz(d,c), zad1.pomnoz(a,f)), zad1.odejmij(zad1.pomnoz(b,d), zad1.pomnoz(e,a))))
	"""
	
	y = zad1.podziel(zad1.odejmij(zad1.pomnoz(d,c), zad1.pomnoz(a,f)), zad1.odejmij(zad1.pomnoz(b,d), zad1.pomnoz(e,a)))
	x = zad1.podziel(zad1.odejmij(f, zad1.pomnoz(e,y)),d)

	return x, y

if "__main__" == __name__:
	print(rrown(-1,-2,0,1,5,12))

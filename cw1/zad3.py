
fib = [1, 1]

_sum = int(input("Zadana suma: "))

def checkSeq(begin):
	sum2 = 0
	while begin < len(fib) and sum2 < _sum:
		sum2 += fib[begin]
		begin += 1
	if sum2 == _sum:
		return True
	else: return False

# Buduje ciag fibbonaciego w tablicy fib,
#	ostatni element jest mniejszy niż _sum
f = 2
while f < _sum:
	fib.append(f)
	f = fib[len(fib) - 1] + fib[len(fib) - 2]


findedBegin = 0
B = False

# Szukamy ciągu
for i in range(0, len(fib)):
	if checkSeq(i):
		findedBegin = i
		# print(i)
		B = True
		break

# Jeśli znalezlismy ciąg to wypisujemy:
if B:
	i = findedBegin
	sum2 = 0
	while sum2 < _sum:
		print(fib[i], end=", ")
		sum2 += fib[i]
		i += 1
else:
	print("Nie ma takiego ciągu")




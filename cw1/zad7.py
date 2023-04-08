
f = [1, 1]

k = int(input())
i = 2
while f[0] * f[1] < k:
	f[i%2] = f[i%2] + f[(i-1)%2]
	i += 1

if f[0] * f[1] == k:
	print("Tak, {} i {}".format(f[0], f[1]))
else:
	print("Nie")

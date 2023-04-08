
k = int(input())
odd  = 1
_sum = 0
n = 0
while _sum < k:
	_sum += odd
	odd += 2
	n += 1

if _sum == k:
	print(n)
else:
	print(n-1)
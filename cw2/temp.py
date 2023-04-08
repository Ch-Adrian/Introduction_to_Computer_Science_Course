end = None
a = [0, 2]

for i in range(1,10):
    b = (1/2)*(a[i]+(1/a[i]))
    a.append(b)
end

print(a)
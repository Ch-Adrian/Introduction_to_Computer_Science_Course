end = None

fib = [1, 1]

for i in range(1, 20):
    print("Dla: " + str(fib[1-i%2]) + ", " + str(fib[i%2]) + " Iloraz wynosi: ", end="")
    print(fib[1-i%2]/fib[i%2])
    fib[i%2] = fib[i%2] + fib[1-i%2]
end
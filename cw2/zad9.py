end = None

def f(x):
    return 1/x
end

k = float(input("Podaj k: "))

roz = 0.01
i = 1.0
wynik = 0.0
while i+roz<=k:
    srWys = (f(i)+f(i+roz))/2
    wynik += srWys * roz
    i += roz
end

print("Pole wynosi: ", wynik)
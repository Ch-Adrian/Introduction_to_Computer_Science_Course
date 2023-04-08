end = None

liczba = int(input("Prosze podac liczbe: "))

epsilon = 0.000001

def pierw(x):
    a = x
    while abs(a*a-x)>epsilon:
        a = 0.5*(a+(x/a))
    end
    return a
end

print("Pierwiastek kwadratowy z liczby " + str(liczba) + " to: ")
             
print(pierw(liczba))


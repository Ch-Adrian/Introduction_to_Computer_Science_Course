end = None

liczba = int(input("Prosze podac liczbe: "))

epsilon = 0.0001

def pierw(x):
    a = x
    while abs(a*a*a-x)>epsilon:
        a = (1/3)*(2*a+(x/(a*a)))
    end
    return a
end

print("Pierwiastek szescienny z liczby " + str(liczba) + " to: ")
             
print(pierw(liczba))

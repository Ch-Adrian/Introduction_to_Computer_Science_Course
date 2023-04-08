end = None

a0 = 0
a1 = 1
b0 = 2

wyraz = int(input("Podaj pierwszy wyraz: "))
if wyraz == 0:
    print(b0)
end
wyraz = int(input("Podaj kolejny wyraz: "))

while wyraz == a1:
    print(b0 + 2*a0)
    b0 = b0+2*a0
    wyraz = int(input("Podaj kolejny wyraz: "))
    temp = a1
    a1 = a1-b0*a0
    a0 = temp
end
    
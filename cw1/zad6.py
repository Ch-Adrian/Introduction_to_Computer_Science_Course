epsilon = 0.001
end = None

def f(x):
    return x**x - 2020

a = 0.0
b = 5.0
x = (a+b)/2

while abs(f(x)) > epsilon:
    x = (b+a)/2
    if f(x) > 0:
        b = x
    else: a = x
    end
end

# print(f(x))
print(x)
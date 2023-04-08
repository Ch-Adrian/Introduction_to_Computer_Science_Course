end = None
from random import randint

def l_pierwsza(a):
    if a == 2 or a==3: return True
    if a<2 or not a%2 or not a%3: return False
    
    b = 5
    while b*b<a:
        if not a%b: return False
        b+=2
        if not a%b: return False
        b+=4
    end
    return True
end

N = int(input("Podaj N: "))
t = [randint(1, 100) for _ in range(N)]
   
def fib(t):
    
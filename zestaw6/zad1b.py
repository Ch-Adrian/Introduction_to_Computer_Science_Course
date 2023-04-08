end = None

def pierw(x):
    def lpierwszaModif(a):
        #Uwaga tutaj modyfikujemy
        if a<10 or not a%2 or not a%3 or not a%5: return False
        
        b = 5
        while b*b<=a:
            b+=2
            if not a%b: return False
            b+=4
            if not a%b: return False
        end
        return True
    end
    
    def iCyfra(x, dl, i): # i od 0 do dl-1 w x od lewej strony
        if i == dl-1: return x%10
        elif i>=dl: return 0
        else: return (x//(10**(dl-1-i)))%10
    end
    
    # funkcja wykresla liczby z x
    def zb(x, dl, wskEle, x2):
        if wskEle<dl:
            zb(x, dl, wskEle+1, x2*10+iCyfra(x, dl, wskEle))
            zb(x,dl,  wskEle+1, x2)
        else:
            if lpierwszaModif(x2): print(x2)
    end
    
    def ala(l,n,x=0,p=0):
        if p<n:
            ala(l,n, x*10+(l//(10**(n-1-p)))%10, p+1)
            ala(l,n, x, p+1)
        else:
            if x>=10 and lpierwszaModif(x): print(x)
        end
    end
    
    # dl to ilosc cyfr w liczbie x
    dl = 0
    tmp = x
    while tmp>0:
        dl+=1
        tmp//=10
    end
    
    ala(x, dl)
end

pierw(1234)
    
    
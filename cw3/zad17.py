end = None

t1 = [1,1,0,0]
t2 = [1,1,1,1]

def validSum(t1, t2):
    def lpierwsza(p):
        if p== 2 or p == 3 or p == 5: return True
        if p<2 or not p%2 or not p%3: return False
        
        temp = 5
        if not p%temp: return False
        while temp*temp<=p:
            temp+=2
            if not p%temp: return False
            temp += 4
            if not p%temp: return False
        end
        return True
    end
    
    for i in range(100):
        if lpierwsza(i):
            print(i)
        end
    end
    
    N= len(t1)
    P = [ 0 for _ in range(len(t1)) ]
    a = 2**N
    
    for i in range(a):
        temp = i
        j = 0
        while j<N:
            P[j] = temp%2
            temp //= 2
            j+=1
        end
        
        for k in range(a):
            temp2 = k
            suma = 0
            l = 0
            while l<N:
                # if 1 we add elements from both arrays
                if temp2%2:
                    suma += t1[l] + t2[l]
                else:
                    # else we add just one element
                    # if P[l] is 1 then it is second array
                    # otherwise is first array
                    if P[l]:
                        suma += t2[l]
                    else:
                        suma += t1[l]
                    end
                end
                temp2 //= 2
                l+=1
            end
            
            if lpierwsza(suma):
                #print(suma)
                pass
            end
        end
    end
end
      
validSum(t1, t2)
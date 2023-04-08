end = None

N = int(input("Podaj N: "))

T = [[0 for _ in range(N)] for _ in range(N) ]

def spirala(T, N):

    n = 1
    for i in range(0, N//2+1):
        
        for j in range(i, N-i):
            T[i][j] = n
            n += 1
        end
        for j in range(i+1, N-i):
            T[j][N-i-1] = n
            n += 1
        end
        for j in range(N-i-2, i-1, -1):
            T[N-i-1][j] = n
            n += 1
        end
        for j in range(N-2-i, i, -1):
            T[j][i] = n
            n += 1
        end
    end
end

def spirala_Ulama(T, N):
    st_k = 0
    st_w = 0
    if N%2:
        st_k = st_w = N//2
    else:
        st_k = N//2 - 1
        st_w = N//2
    end

    n = 1
    counter = 0
    while True:
        counter += 1
        # w prawo
        for i in range(counter):
            if 0 <= st_k < N and 0 <= st_w < N:
                T[st_k][st_w] = n
                n += 1
                st_k += 1
        end

        if n >= N*N: break

        # w góre
        for i in range(counter):
            if 0 <= st_k < N and 0 <= st_w < N:
                T[st_k][st_w] = n
                n += 1
                st_w -= 1
        end

        counter += 1
        if n >= N*N: break

        #w lewo
        for i in range(counter):
            if 0 <= st_k < N and 0 <= st_w < N:
                T[st_k][st_w] = n
                n += 1
                st_k -= 1
        end

        if n >= N*N: break

        # w doł
        for i in range(counter):
            if 0 <= st_k < N and 0 <= st_w < N:
                T[st_k][st_w] = n
                n += 1
                st_w += 1
        end

        if n >= N*N: break
    end
    #T[st_k][st_w] = n
end



def show(T, N):
    for i in range(N):
        for j in range(N):
            print(T[j][i], end=", ")
        end
        print()
    end
end

spirala_Ulama(T, N)
show(T, N)
spirala(T,N)
show(T,N)
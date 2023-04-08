end = None
from random import randint

N = int(input("Podaj liczbę N: "))
T = [ [ randint(1, 10) for _ in range(N)] for _ in range(N)]

def max_iloraz(T, N):

	max_iloraz = 0
	a = b= 0
	for i in range(N):

		for j in range(N):

			s_kol = 0
			s_wiersz = 0

			for k in range(N):
				s_kol += T[k][j]
			end

			for k in range(N):
				s_wiersz += T[i][k]
			end

			#print(s_kol/s_wiersz, end=", ")

			if max_iloraz < s_kol/s_wiersz:
				max_iloraz = s_kol/s_wiersz
				a = i
				b = j
			end
		end
		#print()
	end

	#print(a, b)
	return (a,b)
end

def show(T, N):
    for i in range(N):
        for j in range(N):
            print(T[i][j], end=", ")
        end
        print()
    end
end

#show(T, N)

print(max_iloraz(T,N))



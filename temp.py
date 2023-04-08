end = None
from math import log
from math import ceil

def zpl(liczba, podstawa):
    hex = "0123456789ABCDEF"
    # tab = [0 for _ in range(ceil((log(liczba, podstawa))))]
    tab = [0]*ceil((log(liczba, podstawa)))
    i = 0
    while liczba > 0:
        tab[i] = liczba%podstawa
        liczba //= podstawa
        i += 1
    end
    tab.reverse()
    for j in tab:
        print(hex[j], end="")
    end
end

zpl(10,2)
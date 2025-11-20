# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, list -> List
# Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e,L):
    return [e] + L

# Konsi: List, elemen -> List
# Konsi(L,e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(L,e):
    return L + [e]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) menghasilkan elemen pertama list L
# Realisasi
def FirstElmt(L):
    return L[0]

# LastElmt: List tidak kosong -> elemen
# LastElmt(L) menghasilkan elemen terakhir list L
# Realisasi
def LastElmt(L):
    return L[-1]

# Tail: List tidak kosong -> List
# Tail(L) menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi
def Tail(L):
    return L[1:]

# Head: List tidak kosong -> List
# Head(L) menghasilkan list tanpa elemen terakhir list L, mungkin kosong
# Realisasi
def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List -> Boolean
# IsEmpty(L) true jika list kosong
# Realisasi
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> Boolean
# IsOneElmt(L) true jika list hanya satu elemen
# Realisasi
def IsOneElemt(L):
    if IsEmpty(L):
        return False
    else :
        return Tail(L)==[] and Head(L)==[]

def Pangkat(L):
    if IsOneElemt(L):
        return 0
    else:
        return 1 + Pangkat(Tail(L))
 
def Desimal(X):
    if IsEmpty(X):
        return 0
    elif FirstElmt(X) == '-':
        return -FirstElmt(Tail(X)) * 10 ** Pangkat(Tail(X)) - Desimal(Tail(Tail(X)))
    else:
        return FirstElmt(X) * 10 ** Pangkat(X) + Desimal(Tail(X))
    
def Hasil(X,Y):
    return Desimal(X) + Desimal(Y)

def list(X):
    if X == 0:
        return []
    elif X < 0:
        return Konso(abs(X) % 10, list(abs(X)//10)) + ['-']
    else:
        return Konso(abs(X) % 10, list(abs(X)//10))

def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(LastElmt(L),Inverse(Head(L)))
    
def shrimp(X,Y):
    if Hasil(X,Y) == 0:
        return [0]
    else:
        return Inverse(list(Hasil(X,Y)))

print(list(999))
print(shrimp(['-',1,3],[1,2]))
print(list(100))
print(shrimp([9,9,9,9,9,9,9,9],[1,1]))
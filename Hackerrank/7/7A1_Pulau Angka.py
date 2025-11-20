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

# DEFINISI DAN SPESIFIKASI OPERATOR
# NbElmt: List --> integer
# NbElmt(L) menghasilkan banyaknya elemen list, nol jika kososng
# REALISASI
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# IsMember: elemen, List --> boolean
# IsMember(X,L) benar jika X adalah elemen dari list L
# REALISASI
def IsMember(x, L):
    if IsEmpty(L):
        return False
    else:
        if FirstElmt(L) == x:
            return True
        else:
            return IsMember(x, Tail(L))

def PulauAngka(L1,L2):
    if IsEmpty(L1):
        return []
    elif IsMember(FirstElmt(L1), L2):
        return PulauAngka(Tail(L1),L2)
    else:
        return Konso(FirstElmt(L1), PulauAngka(Tail(L1), L2))
    
print(PulauAngka([-3, 0, 9, 10, 11, 12], [10, 12]))
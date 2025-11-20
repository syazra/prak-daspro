# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elmt, List --> List
# Konso(x, L) memasukan elemen x ke dalam List L dengan x sebagai elemen pertama
def Konso(x, L):
    return [x] + L

# Konsi: List, elmt --> List
# Konsi(x, L) memasukan elemen x ke dalam List L dengan x sebagai elemen terakhir
def Konsi(L, x):
    return L + [x]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List --> elmt
# FirstElmt(L) mengembalikan elemen pertama list L
def FirstElmt(L):
    return L[0]

# LastElmt: List --> elmt
# LastElmt(L) mengembalikan elemen terakhir list L
def LastElmt(L):
    return L[-1]

# Head: List --> List
# Head(L) mengembalikan list L tanpa elemen pertama, mungkin kosong
def Head(L):
    return L[:-1]

# Tail: List --> List
# Tail(L) mengembalikan list L tanpa elemen terakhir, mungkin kosong
def Tail(L):
    return L[1:]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List --> boolean
# IsEmpty(L) bernilai true apabila list L kosong
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> Boolean
# IsOneElmt(L) true jika list hanya satu elemen
# Realisasi
def IsOneElmt(L):
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

def ring(X):
    if X <= 0:
        return []
    else:
        return Konso(X, ring(X-15))
    
print(ring(19))
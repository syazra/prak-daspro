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

def Konversi(X):
    if X == 0:
        return [0]
    elif X ==1:
        return [1]
    else:
        return Konsi(Konversi(X // 2), X % 2)
    
def Sama(X1,X2):
    if NbElmt(X1) == NbElmt(X2):
        return [X1,X2]
    elif NbElmt(X1) < NbElmt(X2):
        return Sama(Konso(0, X1), X2)
    else:
        return Sama(X1, Konso(0, X2))

def Kiri(S):
    return S[0]  

def Kanan(S):
    return S[1]

def And(X1,X2):
    if IsEmpty(X1):
        return []
    elif FirstElmt(X1) == FirstElmt(X2) == 1:
        return Konso(1, And(Tail(X1),Tail(X2)))
    else:
        return Konso(0, And(Tail(X1),Tail(X2)))

def Pangkat(L):
    if IsOneElmt(L):
        return 0
    else:
        return 1 + Pangkat(Tail(L))
    
def TranslateBinary(L):
    if IsEmpty(L):
        return 0
    elif FirstElmt(L) == 0:
        return TranslateBinary(Tail(L))
    else:
        return FirstElmt(L) * 2 ** Pangkat(L) + TranslateBinary(Tail(L))
    
def andBitInt(X1,X2):
    return TranslateBinary(And(Kiri(Sama(Konversi(X1),Konversi(X2))), Kanan(Sama(Konversi(X1),Konversi(X2)))))

def X(l,m):
    return Sama(Konversi(l),Konversi(m))

print(X(7,9))
print(Konversi(9))
print(andBitInt(2,9))
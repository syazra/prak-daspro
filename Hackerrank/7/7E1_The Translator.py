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
# IsEmptyList: List --> boolean
# IsEmptyList(L) bernilai true apabila list L kosong
def IsEmptyList(L):
    return L == []

# IsOneElmt: List --> boolean
# IsOneElmt(L) bernilai true apabila list L hanya berisi 1 elemen.
def IsOneElmt(L):
    return len(L) == 1

def Pangkat(L):
    if IsOneElmt(L):
        return 0
    else:
        return 1 + Pangkat(Tail(L))
    
def TranslateBinary(L):
    if IsEmptyList(L):
        return 0
    elif FirstElmt(L) == 0:
        return TranslateBinary(Tail(L))
    else:
        return FirstElmt(L) * 2 ** Pangkat(L) + TranslateBinary(Tail(L))
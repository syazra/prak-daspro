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

def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    elif FirstElmt(L) > LastElmt(L):
        return MaxElmt(Head(L))
    else:
        return MaxElmt(Tail(L))
    
def Remove(L,X):
    if IsEmptyList(L):
        return []
    elif X == FirstElmt(L):
        return Tail(L)
    else:
        return Konso(FirstElmt(L), Remove(Tail(L),X))

def MaxL(L):
    if IsEmptyList(L):
        return []
    else:
        return Konso(MaxElmt(L), MaxL(Remove(L,MaxElmt(L))))

def BigDifference(L):
    if IsEmptyList(L):
        return []
    elif IsOneElmt(L):
        return L
    else:
        return Konso(LastElmt(MaxL(L)), Konso(FirstElmt(MaxL(L)), BigDifference(Remove(Head(MaxL(L)),MaxElmt(L)))))

print(BigDifference([2,6,4,6,9,3,3,4,9]))
    
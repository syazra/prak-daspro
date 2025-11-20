#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, Set -> Set
# Konso(e,S) menghasilkan sebuah Set dari e dan S dengan e sebagai elemen pertama
# Realisasi
def Konso(e,S):
    return [e] + S

# Konsi: Set, elemen -> Set
# Konsi(S,e) menghasilkan sebuah Set dari S dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(S,e):
    return S + [e]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: Set tidak kosong -> elemen
# FirstElmt(S) menghasilkan elemen pertama Set S
# Realisasi
def FirstElmt(S):
    return S[0]

# LastElmt: Set tidak kosong -> elemen
# LastElmt(S) menghasilkan elemen terakhir Set S
# Realisasi
def LastElmt(S):
    return S[-1]

# Tail: Set tidak kosong -> Set
# Tail(S) menghasilkan Set tanpa elemen pertama Set S, mungkin kosong
# Realisasi
def Tail(S):
    return S[1:]

# Head: Set tidak kosong -> Set
# Head(S) menghasilkan Set tanpa elemen terakhir Set S, mungkin kosong
# Realisasi
def Head(S):
    return S[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: Set -> Boolean
# IsEmpty(S) true jika Set kosong
# Realisasi
def IsEmpty(S):
    return S == []

# IsOneElmt: Set -> Boolean
# IsOneElmt(S) true jika Set hanya satu elemen
# Realisasi
def IsOneElemt(S):
    if IsEmpty(S):
        return False
    else :
        return Tail(S)==[] and Head(S)==[]

def IsMember(x, L):
    if IsEmpty(L):
        return False
    else:
        return IsMember(x, Tail(L)) or FirstElmt(L) == x

def MakeSet(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet(Tail(L))
        else:
            return Konso(FirstElmt(L), MakeSet(Tail(L)))

def Union(S1, S2):
    return S1 + S2

def MinElmt(S):
    if IsOneElemt(S):
        return FirstElmt(S)
    elif FirstElmt(S) < LastElmt(S):
        return MinElmt(Head(S))
    else:
        return MinElmt(Tail(S))
    
def Remove(S, X):
    if IsEmpty(S):
        return []
    elif X == FirstElmt(S):
        return Tail(S)
    else:
        return Konso(FirstElmt(S), Remove(Tail(S), X))

def Min(S):
    if IsEmpty(S):
        return []
    else:
        return Konso(MinElmt(S), Min(Remove(S, MinElmt(S))))

def Kiri1(S, X):
    if IsEmpty(S) or X == 0:
        return []
    else:
        return Konsi(Kiri1(Head(S), X-1), LastElmt(S))

def Kiri(S, X):
    if IsEmpty(S) or X == 0:
        return []
    else:
        if LastElmt(S) == X:
            return Kiri1(Head(S), X)
        else:
            return Kiri(Head(S), X)

def Kanan1(S, X):
    if IsEmpty(S) or X == 0:
        return []
    else:
        return Konso(FirstElmt(S), Kanan1(Tail(S), X-1))
    
def Kanan(S, X):
    if IsEmpty(S) or X == 0:
        return []
    else:
        if FirstElmt(S) == X:
            return Kanan1(Tail(S), X)
        else:
            return Kanan(Tail(S), X)

def Bersih(S1, S2, X):
    if IsMember(X, S2):
        return RemoveS(Malas(S1, S2, X), Min(Union(S1, S2)))
    else:
        return MakeSet(Min(Kiri(Min(Union(S1, S2)), X) + [X] + Kanan(Min(Union(S1, S2)), X) + S1))

def RemoveS(S1, S2):
    if IsEmpty(S1):
        return S2
    else:
        if FirstElmt(S1) == FirstElmt(S2):
            return RemoveS(Tail(S1), Tail(S2))
        else:
            return Konso(FirstElmt(S2), RemoveS(S1, Tail(S2)))
 
def Malas(S1, S2, X):
    if IsMember(X, S2):
        return MakeSet(Min(Kiri(Min(Union(S1, S2)), X) + [X] + Kanan(Min(Union(S1, S2)), X) + S2))
    else:
        return RemoveS(Bersih(S1, S2, X), Min(Union(S1, S2)))

print(Bersih([1,6,5,3,2,0],[7,4,8], 2))
print(Malas([1,6,5,3,2,0],[7,4,8], 2))
print(Bersih([0,1,2,3], [4, 5, 6, 7, 8], 3))
print(Bersih([10, 25, 30, 15, 40, 50, 60, 5, 12, 18], [20, 35, 45, 55, 65, 7, 17, 27, 37, 47], 5))
print(Malas([10, 25, 30, 15, 40, 50, 60, 5, 12, 18], [20, 35, 45, 55, 65, 7, 17, 27, 37, 47], 5))
print(Bersih([10, 3, 1],[8, 4, 5, 6, 7], 4))
print(Malas([10, 3, 1],[8, 4, 5, 6, 7], 4))
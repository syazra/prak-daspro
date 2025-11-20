# Tanggal: 12, November 2024
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def konsLo(L, S):
    return [L] + S

def konsLi(S, L):
    return S + [L]

# DEFINISI DAN SPESIFIKASI SELEKTOR
def FirstList(S):
    return S[0]

def TailList(S):
    return S[1:]

def LastList(S):
    return S[-1]

def HeadList(S):
    return S[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
def IsEmpty(S):
    return S == []

def IsAtom(S):
    return type(S) != list

def IsList(S):
    return type(S) == list

def IsOneElmt(S):
    return len(S) == 1

def Inverse(S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(LastList(S)):
            return konsLo(LastList(S), Inverse(HeadList(S)))
        else:
            return konsLo(Inverse(LastList(S)), Inverse(HeadList(S)))

def ToListBiasa(S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            return konsLo(FirstList(S), ToListBiasa(TailList(S)))
        else:
            return ToListBiasa(FirstList(S)) + ToListBiasa(TailList(S))

def Rember_V1(X, L):
    if IsEmpty(L): # Basis
        return []
    else: # Rekurens
        if FirstList(L) == X:
            return TailList(L)
        else:
            return konsLo(FirstList(L), Rember_V1(X, TailList(L)))
        
# MaxElmt(H) mengembalikan elemen maksimum dari set H
# REALISASI
def MaxElmt(H):
    if IsOneElmt(H):
        return FirstList(H)
    else:
        if FirstList(H) > LastList(H):
            return MaxElmt(HeadList(H))
        else:
            return MaxElmt(TailList(H))
# MaxH: set --> set
# MaxH(H) mengurutkan set H dari elemen maksimum menuju minimum
# REALISASI
def MaxH(H):
    if IsEmpty(H):
        return []
    else:
        return konsLo(MaxElmt(H), MaxH(Rember_V1(MaxElmt(H), H)))

def remove(L1, L2):
    if IsEmpty(L1):
        return L2
    else:
        if IsAtom(FirstList(L2)):
            return remove(TailList(L1), TailList(L2))
        else:
            return remove(FirstList(L1), FirstList(L2)) + remove(TailList(L1), TailList(L2))
 
def Ubah(S1, S2):
    if IsEmpty(S2):
        return []
    else:
        if IsAtom(FirstList(S2)):
            return konsLo(FirstList(S1), Ubah(TailList(S1), TailList(S2)))
        else:
            return konsLo(Ubah(S1, FirstList(S2)), Ubah(remove(ToListBiasa(Ubah(S1, FirstList(S2))), ToListBiasa(S1)), TailList(S2)))
        
def RiftTraverse(S):
    return Ubah(ToListBiasa(Inverse(S)), S)

print(RiftTraverse([[[[9], 8]],[3], [1, 0]]))
print(RiftTraverse([[4,2,9], 10, [[[5,9]], 7, [[7, 2]]], 1, 9,[0]]))
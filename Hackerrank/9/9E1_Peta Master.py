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

# IsOneElmt: list of list --> boolean
# IsOneElmt(S) benar jika S hanya memiliki satu elemen
def IsOneElmt(S):
    if IsEmpty(S):
        return False
    else:
        return TailList(S) == [] and HeadList(S) == []

# Max: list of list --> elemen
# Max(S) menghasilkan elemen maksimum di dalam list of list S   
def Max(S):
    if IsEmpty(S):
        return 0
    elif IsOneElmt(S):
        if IsAtom(FirstList(S)):
            return FirstList(S)
        else:
            return Max(FirstList(S))
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) > Max(TailList(S)):
                return FirstList(S)
            else:
                return Max(TailList(S))
        else:
            if Max(FirstList(S)) > Max(TailList(S)):
                return Max(FirstList(S))
            else:
                return Max(TailList(S))

# SumLoL: list of list --> integer
# SumLoL(S) menghitung penjumlahan semua elemen dalam list of list S
def SumLoL(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) > 0:
                return 1 + SumLoL(TailList(S))
            else:
                return SumLoL(TailList(S))
        else:
            return SumLoL(FirstList(S)) + SumLoL(TailList(S))
        
def LuasDaerah(S):
    return [SumLoL(S), Max(S)]

print(LuasDaerah([
    [1,0,1,0,0,0,0],
    [1,1,1,1,0,0,0],
    [3,2,1,0,0,0,0],
    [4,4,2,1,0,0,0],
    [2,3,2,1,1,0,0]
]))
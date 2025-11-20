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

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(TailList(L))
    
def NbEmpty(S):
    if IsEmpty(S):
        return 0
    else:
        if IsEmpty(FirstList(S)):
            return 1 + NbEmpty(TailList(S))
        else:
            return NbEmpty(TailList(S))
        
def KacangRisu(L, S):
    if IsEmpty(S):
        return []
    else:
        if NbElmt(L) == NbEmpty(S):
            if IsEmpty(FirstList(S)):
                return [[FirstList(L)]] + KacangRisu(TailList(L), TailList(S))
            else:
                return konsLo(FirstList(S), KacangRisu(L, TailList(S)))
        else:
            return 'Mending Pulang'

print(KacangRisu([1,2,9, 3], [[],[4,5,6],[],[4,9],[], [9,2], []]))
print(NbEmpty([[],[1,2,3],[],[4,9],[]]))

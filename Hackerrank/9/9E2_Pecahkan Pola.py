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

def SumLoL(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            return FirstList(S) + SumLoL(TailList(S))
        else:
            return SumLoL(FirstList(S)) + SumLoL(TailList(S))
        
def MemecahkanPola(x, S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) % x == 0:
                return MemecahkanPola(x, TailList(S))
            else:
                return konsLo(FirstList(S), MemecahkanPola(x, TailList(S)))
        else:
            if SumLoL(FirstList(S)) % x == 0:
                return MemecahkanPola(x, TailList(S))
            else:
                return konsLo(MemecahkanPola(x, FirstList(S)), MemecahkanPola(x, TailList(S)))

print(SumLoL([20,[30],50]))               
print(MemecahkanPola(100, [1,2,4,[25,[1,[20,[30],50]]],50]))
print(MemecahkanPola(12, [1, [9, [0, [1]], 2], 4]))
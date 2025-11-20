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

def IsEqual(L1, L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return True
    elif IsEmpty(L1) or IsEmpty(L2):
        return False
    else:
        if FirstList(L1) == FirstList(L2):
            return IsEqual(TailList(L1), TailList(L2))
        else:
            return False

# DEFINISI DAN SPESIFIKASI
def IsMemberLS(L, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            return IsMemberLS(L, TailList(S))
        else:
            if IsEqual(L, FirstList(S)):
                return True
            else:
                return IsMemberLS(L, TailList(S))

def IsEqS(S1, S2):
    if IsEmpty(S1) and IsEmpty(S2):
        return True
    elif IsEmpty(S1) or IsEmpty(S2):
        return False
    else:
        if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
            if FirstList(S1) == FirstList(S2):
                return IsEqS(TailList(S1), TailList(S2))
            else:
                return False
        elif IsList(FirstList(S1)) and IsList(FirstList(S2)):
            return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(TailList(S1), TailList(S2))
        else:
            return False

def IsMemberS(x, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            if x == FirstList(S):
                return True
            else:
                return IsMemberS(x, TailList(S))
        else:
            return IsMemberS(x, FirstList(S)) or IsMemberS(x, TailList(S))

def tolist(X):
    if X == 0:
        return []
    else:
        return konsLi(tolist(X // 10), X % 10)

def HateAllN(S, N):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            if N == FirstList(S) or FirstList(S) % N == 0 or IsMemberS(N, tolist(FirstList(S))):
                return HateAllN(TailList(S), N)
            else:
                return konsLo(FirstList(S), HateAllN(TailList(S), N))
        else:
            return konsLo(HateAllN(FirstList(S), N), HateAllN(TailList(S), N))
        
print(HateAllN([[1], [[9,8],9,[8],[[1], 5], 2, 16]], 1))
print(HateAllN([[18], [[[10, 9, 59, [[897, 2, [9806]]]], 63, 0, [7]]]], 9))
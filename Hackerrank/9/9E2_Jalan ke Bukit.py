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

def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        return IsMember(X,TailList(L)) or X == FirstList(L)

def IsMemberLoL(X, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) == X:
                return True
            else:
                return IsMemberLoL(X, TailList(S))
        else:
            return IsMemberLoL(X, FirstList(S)) or IsMemberLoL(X, TailList(S))
        
def ElmtKe(X, S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) == X:
                return 1
            else:
                return 1 + ElmtKe(X, TailList(S))
        else:
            if IsMemberLoL(X, FirstList(S)):
                return 1
            else:
                return 1 + ElmtKe(X, TailList(S))

def Delete(X, S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            return Delete(X, TailList(S))
        else:
            if IsMemberLoL(X, FirstList(S)):
                return FirstList(S)
            else:
                return Delete(X, TailList(S))
    
def JalanBukit(X, S):
    if IsEmpty(S) or not IsMemberLoL(X, S):
        return []
    else:
        if IsMember(X, S):
            return [ElmtKe(X, S)]
        else:
            return konsLo(ElmtKe(X, S), JalanBukit(X, Delete(X, S)))


print(JalanBukit(5, [9, [8, [[91], [99]]], [1, [9, [98]]], [2, [88, [5]]]]))
print(JalanBukit(0, [1, [2, [[[[[8], 0]]], 4], 5], 6]))


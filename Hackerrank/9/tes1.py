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

def Isone(S):
    return len(S) == 1

def IsAtom(S):
    return type(S) != list

def IsList(S):
    return type(S) == list

def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        return IsMember(X,TailList(L)) or X == FirstList(L)

def ToListBiasa(S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            return konsLo(FirstList(S), ToListBiasa(TailList(S)))
        else:
            return konsLo(hitung(FirstList(S)), ToListBiasa(TailList(S)))
              
def hitung(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            return FirstList(S) + hitung(TailList(S))
        else:
            return hitung(FirstList(S)) + hitung(TailList(S))

def kingmod(N, S):
    if IsEmpty(S):
        return []
    else:
        return konsLo(FirstList(ToListBiasa(S)) % N, kingmod(N, TailList(ToListBiasa(S))))
        
def kosong(S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            return kosong(TailList(S))
        elif FirstList(S) == []:
            return True
        else:
            return kosong(FirstList(S)) or kosong(TailList(S))

def KingModulo2(N, S):
    if IsEmpty(S) or N == 0 or kosong(S):
        return -999
    else:
        return kingmod(N, S)       


print(KingModulo2(8, [9, [[[[[99, [9, [99]], [[[8]]]]]]]], [8, [9, [0]]], 71]))
print(KingModulo2(-10, [9, [9, [-88]], 9, [2, [[[[[[[[[[[[[[93, -90]]]]]]]]]]]]]]], 0, 1, [[1, 2]]]))
print(KingModulo2(8, [[[[[[[[[[9, 6]]]]]]]]]]))
print(KingModulo2(-7, [9, [9, []], 9, [2, [[[[[[[[[[[[[[]]]]]]]]]]]]]]], 0, 1, [[1, 2]]]))
# Input: N = 10, List of List bersarang
print(KingModulo2(10, [5, [[[[[15, [25, [35]], [[[45]]]]]]]], [55, [65, [75]]], 85]))
# Output: [5, 5, 5, 5, 5, 5, 5, 5]
print(KingModulo2(6, [12, -2, -7, 80, 4, 90]))
# Output: [2, 7, 7, 0, 0]
print(KingModulo2(100, [[[[[[[[[[999]]]]]]]]]]))
# Output: [99]
print(KingModulo2(10, [[0, [0, [0]]], 0, [[[0]]], []]))
# Output: [0, 0, 0, 0, 0, 0]


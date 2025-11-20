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

# def Kosong(S):
#     if IsEmpty(S):
#         return 0
#     else:
#         return 1 + Kosong(TailList(S))

# def TidakKosong(S):
#     if IsEmpty(S):
#         return 0
#     elif IsList(FirstList(S)) and not IsEmpty(FirstList(S)):
#         return 1 + TidakKosong(TailList(S))
#     else:
#         return TidakKosong(TailList(S))
    
# def MatryoshkaBox(S):
#     return 1 + Kosong(S) + TidakKosong(S)

def tes(x):
    if IsEmpty(x):
        return 0
    elif FirstList(x) == []:
        return 1 + tes(TailList(x))
    else:
        return 1 + tes(FirstList(x)) + tes(TailList(x))
    
def boxSummoner(S):
    return 1 + tes(S)

print(boxSummoner([[[[[[],[[]]],[[[[]]]]],[[[[[],[]]],[]]],[[[[[[]]]],[[[],[]]]]],[[[],[[]]],[[[[[[],[]]]]]]],[[[[[[[]]]]]]]]]]))
print(boxSummoner([[[[[]]]], [[], [[], [[[]]], []]]]))
print(boxSummoner([[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[], [[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], []]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]))

print(len([[[[[]]]]]))
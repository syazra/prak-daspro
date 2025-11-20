def makePN(A, PN):
    return [A, PN]

def Akar(T):
    return T[0]

def Anak(T):
    return T[1]

def IsTreeNEmpty(PN):
    return PN == []

def IsOneElmt(PN):
    return (IsTreeNEmpty(PN) == False) and (IsTreeNEmpty(Anak(PN)) == True)

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list --> list of list
# KonsLo(L, S) membentuk list baru dengan list (L) yang diberikan sebagai elemen pertama list of list (S)
def KonsLo(L, S):
    return [L] + S

# KonsLi: list of list, list --> list of list
# KonsLi(S, L) membentuk list baru dengan list (L) yang diberikan sebagai elemen terakhir list of list (S)
def KonsLi(S, L):
    return S + [L]

#====================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: list of list tidak kosong --> list
# FirstList(S) menghasilkan elemen pertama list of list S, mungkin sebuah list atau atom
def FirstList(S):
    return S[0]

# TailList: list of list tidak kosong --> list of list
# TailList(S) menghasilkan "sisa" list of list S tanpa elemen pertamanya
def TailList(S):
    return S[1:]

# LastList: list of list tidak kosong --> list
# LastList(S) menghasilkan elemen terakhir list of list S, mungkin sebuah list atau atom
def LastList(S):
    return S[-1]

# HeadList: list of list tidak kosong --> list of list
# HeadList(S) menghasilkan "sisa" list of list S tanpa elemen terakhirnya
def HeadList(S):
    return S[:-1]

#====================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST
# IsAtom: list of list --> boolean
# IsAtom(S) benar jika S adalah sebuah atom
def IsAtom(S):
    return type(S) != list

# IsList: list of list --> boolean
# IsList(S) benar jika S adalah sebuah list
def IsList(S):
    return type(S) == list

# IsEmpty: list of list --> boolean
# IsEmpty(S) benar jika S adalah list of list kosong
def IsEmpty(S):
    return S == []

# IsOneElmt: list of list --> boolean
# IsOneElmt(S) benar jika S hanya memiliki satu elemen
def IsOneElmt(S):
    if IsEmpty(S):
        return False
    else:
        return TailList(S) == [] and HeadList(S) == []

# IsMemberS: elemen, list of list --> boolean
# IsMemberS(x, S) benar jika elemen x ada di dalam list of list S
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

def Child(X, P):
    if IsTreeNEmpty(P):
        return []
    elif IsMemberS(X, Anak(P)[0]):
        return Anak(P)
    else:
        return GetHelp(X, Anak(P))
    
def GetHelp(X, P):
    if IsTreeNEmpty(P):
        return []
    else:
        return Child(X, P[0]) + GetHelp(X, P[1:])

print(Child("Silvani", makePN("Ridho", [makePN("Silvani", [makePN("Nuha",[]), makePN("Syahrafi",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])])))

def PrintTreeNAryHelp(T, sisa, indent):
    print(indent + str(Akar(T)))
    if not IsEmpty(Anak(T)):
        PrintTreeNAryHelp(FirstList(Anak(T)), TailList(Anak(T)), indent + '\t')
    if not IsEmpty(sisa):
        PrintTreeNAryHelp(FirstList(sisa), TailList(sisa), indent)

def PrintTreeNAry(T):
    PrintTreeNAryHelp(T, [], '')
    
PrintTreeNAry(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]))

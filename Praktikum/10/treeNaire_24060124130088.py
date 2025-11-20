# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def MakePN(A, PN):
    return [A, PN]

# DEFINISI DAN SPESIFIKASI SELEKTOR
def Akar(PN):
    return PN[0]

def Anak(PN):
    return PN[1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
def IsTreeNEmpty(PN):
    return PN == []

def IsOneElmt(PN):
    return (IsTreeNEmpty(PN) == False) and (IsTreeNEmpty(Anak(PN)) == True)

# DEFINISI DAN SPESIFIKASI OPERATOR
def NbElmt(PN):
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN):
        return 1
    else:
        return 1 + NbElmt(Anak(PN)[0]) + NbElmtChild(Anak(PN)[1:])

def NbElmtChild(PN):
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NbElmt(PN[0]) + NbElmtChild(PN[1:])

def NbDaun(PN):
    if IsTreeNEmpty(PN):
        return 0
    elif IsOneElmt(PN) and IsTreeNEmpty(Anak(PN)):
        return 1
    else:
        return NbDaunChild(Anak(PN))
    
def NbDaunChild(PN):
    if IsTreeNEmpty(PN):
        return 0
    else:
        return NbDaun(PN[0]) + NbDaunChild(PN[1:])

def SearchX(X, PN):
    if IsTreeNEmpty(PN):
        return False
    elif IsOneElmt(PN):
        return X == PN[0]
    elif X == Akar(PN):
        return True
    else:
        return SearchX(X, Anak(PN)[0]) or SearchChildX(X, Anak(PN)[1:])
    
def SearchChildX(X, PN):
    if IsTreeNEmpty(PN):
        return False
    else:
        return SearchX(X, PN[0]) or SearchChildX(X, PN[1:])

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

# IsEmpty: list of list --> boolean
# IsEmpty(S) benar jika S adalah list of list kosong
def IsEmpty(S):
    return S == []

def PrintTreeNAryHelp(T, sisa, indent):
    print(indent + str(Akar(T)))
    if not IsEmpty(Anak(T)):
        PrintTreeNAryHelp(FirstList(Anak(T)), TailList(Anak(T)), indent + '\t')
    if not IsEmpty(sisa):
        PrintTreeNAryHelp(FirstList(sisa), TailList(sisa), indent)

def PrintTreeNAry(T):
    PrintTreeNAryHelp(T, [], '')

def SearchXTree(X, PN):
    if IsTreeNEmpty(PN):
        return False
    elif IsOneElmt(PN):
        return X == FirstList(PN)
    elif X == Akar(PN):
        return True
    else:
        return SearchXTree(X, FirstList(Anak(PN))) or SearchXChild(X, TailList(Anak(PN)))
        
def SearchXChild(X, PN):
    if IsTreeNEmpty(PN):
        return False
    else:
        return SearchXTree(X, FirstList(PN)) or SearchXChild(X, TailList(PN))
    
PN1 = MakePN('A', [MakePN('B', [MakePN('D', []), MakePN('E', []), MakePN('F', [])]), MakePN('C', [MakePN('G', []), MakePN('H', [MakePN('I', [])])])])
PN2 = MakePN('K', [MakePN('C', []), MakePN('F', [MakePN('D', [MakePN('W', [MakePN('Y', [MakePN('9', [])])]), MakePN('3', []), MakePN('B', [])]), MakePN('2', [])]), MakePN('7', [MakePN('B', [MakePN('S', [])])])])
T = MakePN("Ridho",[MakePN("Silvani",[MakePN("Nuha",[]), MakePN("Syahrafi",[])]), MakePN("Rendi",[MakePN("Fikhrul",[])]), MakePN("Ruth",[MakePN("Aji",[])]), MakePN("Eko",[MakePN("Raffi",[])])])
print(PN2)
PrintTreeNAry(PN2)
print(FirstList(PN1))
print(IsOneElmt(PN1))
print(NbElmt(PN2))
print(NbDaun(PN1))
print(SearchXTree('9', PN2))
print(SearchXTree('K', PN2))
print(SearchXTree('Nuha', T))

PrintTreeNAry(MakePN("Ridho",[MakePN("Silvani",[MakePN("Nuha",[]), MakePN("Syahrafi",[MakePN("Ega", [])]), MakePN("Noci",[])]), MakePN("Rendi",[MakePN("Fikhrul",[])]), MakePN("Ruth",[MakePN("Aji",[])]), MakePN("Eko",[MakePN("Raffi",[])])]))

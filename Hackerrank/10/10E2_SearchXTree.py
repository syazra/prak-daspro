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

def SearchXTree(X, PN):
    if IsTreeNEmpty(PN):
        return False
    elif IsOneElmt(PN):
        return X == Akar(PN)
    elif X == Akar(PN):
        return True
    else:
        return SearchXChild(X, Anak(PN))
        
def SearchXChild(X, PN):
    if IsTreeNEmpty(PN):
        return False
    else:
        return SearchXTree(X, PN[0]) or SearchXChild(X, PN[1:])
    
print(SearchXTree("Raffi", makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]),
            makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]),
            makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]),
            makePN("Eko",[makePN("Raffi",[])])])))

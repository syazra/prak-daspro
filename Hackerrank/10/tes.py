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

def KonsLo(L, S):
    return [L] + S

def KonsLi(S, L):
    return S + [L]

def FirstList(S):
    return S[0]

def TailList(S):
    return S[1:]

def LastList(S):
    return S[-1]

def HeadList(S):
    return S[:-1]

def IsEmpty(S):
    return S == []

# Search function for element X in tree PN
def SearchXTree(X, PN):
    if IsTreeNEmpty(PN):
        return False
    elif IsOneElmt(PN):
        return X == FirstList(PN)
    elif X == Akar(PN):
        return True
    else:
        # Search in the children of the root node
        return SearchXChild(X, Anak(PN))

# Recursive search in children of a node
def SearchXChild(X, PN):
    if IsTreeNEmpty(PN):
        return False
    else:
        return SearchXTree(X, FirstList(PN)) or SearchXChild(X, TailList(PN))
    
# Saudara: find the siblings of X in tree T
def Saudara(X, T):
    if IsTreeNEmpty(T) or X == Akar(T) or not SearchXTree(X, T):
        return []  # No siblings if the tree is empty or root is X or X not found
    else:
        return GetHelp(X, Anak(T))

# GetHelp: helper function to get siblings of X
def GetHelp(X, T):
    if IsTreeNEmpty(T):
        return []  # No more children, return empty list
    else:
        # If X is found as the first child, return the rest of the children
        if X == Akar(FirstList(T)):
            return [Akar(FirstList(T)) for T in TailList(T)]
        else:
            # Recursively check the rest of the children
            return GetHelp(X, TailList(T))

T = makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])])
print(Saudara("Silvani", T))
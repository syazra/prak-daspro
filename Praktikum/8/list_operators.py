def Konso(e, L):
    return [e] + L

def Konsi(L, e):
    return L + [e]

def FirstElmt(L):
    return L[0]

def Tail(L):
    return L[1:] 

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def IsEmpty(L):
    return L == []

def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []
    
def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        return IsMember(X, Tail(L)) or X == FirstElmt(L)

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))
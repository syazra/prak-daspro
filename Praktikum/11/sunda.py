def MakePN(A,L,R):
    return [A,L,R]

def IsEmpty(PN):
    return PN == None

def Akar(PN):
    return PN[0]

def Left(PN):
    return PN[1]

def Right(PN):
    return PN[2]

def IsOneElmt(PN):
    return IsEmpty(Left(PN)) and IsEmpty(Right(PN)) and not IsEmpty(PN)

def IsBiner(PN):
    return not IsEmpty(Left(PN)) and not IsEmpty(Right(PN))

def IsUnerLeft(PN):
    return not IsEmpty(Left(PN)) and IsEmpty(Right(PN))

def IsUnerRight(PN):
    return IsEmpty(Left(PN)) and not IsEmpty(Right(PN))

def IsEqual(X,PN):
    return X == PN

def IsSimpul(P,X):
    if IsOneElmt(P):
        return IsEqual(X,Akar(P))
    elif IsEmpty(P):
        return False
    else:
        if IsEqual(X,Akar(P)):
            return True
        elif IsBiner(P):
            return IsSimpul(Left(P),X) or IsSimpul(Right(P),X)
        elif IsUnerLeft(P):
            return IsSimpul(Left(P),X)
        else: # IsUnerRight(P)
            return IsSimpul(Right(P),X)

print(IsSimpul(MakePN(4,MakePN(5,None,None),None),5))
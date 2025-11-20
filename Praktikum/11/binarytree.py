def MakeBN(A, L, R):
    return [A, L, R]

def Akar(BN):
    return BN[0]

def Left(BN):
    return BN[1]

def Right(BN):
    return BN[2]

def IsEmpty(BN):
    return BN == [] or BN == None

def IsOneElmt(BN):
    return IsEmpty(Left(BN)) and IsEmpty(Right(BN)) and not IsEmpty(BN)

def IsBiner(BN):
    return not IsEmpty(Left(BN)) and not IsEmpty(Right(BN))

def IsUnerLeft(BN):
    return not IsEmpty(Left(BN)) and IsEmpty(Right(BN))

def IsUnerRight(BN):
    return IsEmpty(Left(BN)) and not IsEmpty(Right(BN))

def IsSimpul(X, BN):
    if IsEmpty(BN) or IsOneElmt(BN):
        return False
    elif X == Akar(BN):
        return True
    else:
        if IsBiner(BN):
            return IsSimpul(X, Left(BN)) or IsSimpul(X, Right(BN))
        elif IsUnerLeft(BN):
            return IsSimpul(X, Left(BN))
        elif IsUnerRight(BN):
            return IsSimpul(X, Right(BN))

def maxdaun(P):
    if IsOneElmt(P):
        return [Akar(P)]
    else:
        if IsBiner(P):
            return maxdaun(Left(P)) + maxdaun(Right(P))
        elif IsUnerLeft(P):
            return maxdaun(Left(P))
        else:
            return maxdaun(Right(P))
print(maxdaun(MakeBN(7, MakeBN(2, (MakeBN(8, None, None)), None), MakeBN(5, None, None))))
print(IsEmpty(None))
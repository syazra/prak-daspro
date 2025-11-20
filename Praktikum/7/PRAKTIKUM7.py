def Konso(x, L):
    return [x] + L

def Konsi(L, x):
    return L + [x]

def FirstElmt(L):
    return L[0]

def LastElmt(L):
    return L[-1]

def Head(L):
    return L[:-1]

def Tail(L):
    return L[1:]

def IsEmptyList(L):
    return L == []

def IsOneElmt(L):
    return len(L) == 1

def NbElmt(L):
    if L == []:
        return 0
    else: 
        return 1 + NbElmt(Tail(L))


def SumElmt(L):
    if IsEmptyList(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))
    
def AvgElmt(L):
    return SumElmt(L) / NbElmt(L)

def Konkat(L1, L2):
    if IsEmptyList(L2):
        return L1
    else:
        return Konkat(Konsi(L1, FirstElmt(L2)), Tail(L2))
    
def ElmntkeN(N,L):
    if N==1:
        return FirstElmt(L)
    else:
        return ElmntkeN(N-1, Tail(L))

def IsMember(X,L):
    if IsEmptyList(L):
        return False
    elif X == FirstElmt(L):
        return True
    else:
        return IsMember(X, Tail(L))

def Inverse(L):
    if IsEmptyList(L):
        return []
    else:
        return Konsi(Inverse(Tail(L)), FirstElmt(L))

def IsPalindromx (L) :
    if (L == []) or (L == [FirstElmt(L)]) :
        return True
    else :
        if (FirstElmt(L) == LastElmt(L)) :
            return IsPalindromx(Head(Tail(L)))
        else :
            return False

def Copy(L) :
    if IsEmptyList(L) :
        return []
    else :
        return Konso(FirstElmt(L),Copy(Tail(L)))

def AddList(L1,L2):
    if IsEmptyList(L1) and IsEmptyList(L2):
        return []
    elif IsEmptyList(L1):
        return L2
    elif IsEmptyList(L2):
        return L1
    else:
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

def MaxElmt(L):
    if IsOneElmt(L):
        return(FirstElmt(L))
    elif FirstElmt(L) > LastElmt(L):
        return MaxElmt(Head(L))
    else:
        return MaxElmt(Tail(L))

def max(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    else:
        if FirstElmt(L) > max(Tail(L)):
            return FirstElmt(L)
        else:
            return max(Tail(L))
    
def jumlahx(L,x):
    if IsEmptyList(L):
        return 0
    else:
        if FirstElmt(L) == x:
            return 1 + jumlahx(Tail(L),x)
        else:
            return jumlahx(Tail(L),x)
        
def maxNb(L):
    return (max(L), jumlahx(L, max(L)))


# APLIKASI
print(MaxElmt([1,2,13,3,4]))
print(SumElmt([1,2,3,4]))
print(AvgElmt([1,2,3,4]))
print(Konkat([1,2,3,4], [9, 10]))
print(ElmntkeN(2,[1,2,3,4]))
print(IsMember(3,[1,2,0,4]))
print(Inverse([1,2,3,4,5]))
print(IsPalindromx(['K','A','K','A','N']))
print(Copy([1,2,3,4,5]))
print(AddList([1,3,7], [-1, -2, 5, 2]))
print(maxNb([5,6,3,4,6]))
# DEFINISI DAN SEPSIFIKASI KONSTRUKTOR
# Konso: elemen, List --> List
# Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# REALISASI
def Konso(e,L):
    return [e] + L

# Konsi: List, elemen --> List
# Konsi(L,e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# REALISASI
def Konsi(L,e):
    return L + [e]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong --> elemen
# FirstElmt(L) mengembalikan elemen pertama list L
# REALISASI
def FirstElmt(L):
    return L[0]

# Tail: List tidak kosong --> List
# Tail(L) mengembalikan list tanpa elemen pertama list L, mungkin kosong
# REALISASI
def Tail(L):
    return L[1:] 

# LastElmt: List tidak kososng --> elemen
# LastElmt(L) mengembalikan elemen terakhir pada list L
# REALISASI
def LastElmt(L):
    return L[-1]

# Head: List tidak kosong --> List
# Head(L) mengembalikan list tanpa elemen terakhir list L, mungkin kosong
# REALISASI
def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List --> boolean
# IsEmpty(L) benar jika list kosong
# REALISASI
def IsEmpty(L):
    return L == []

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list --> list of list
# KonsLo(L, S) membentuk list baru dengan list (L) yang diberikan sebagai elemen pertama list of list (S)
def KonsLo(L, S):
    return [L] + S

# KonsLi: list of list, list --> list of list
# KonsLi(S, L) membentuk list baru dengan list (L) yang diberikan sebagai elemen terakhir list of list (S)
def KonsLi(S, L):
    return S + [L]

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

# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST
# IsAtom: list of list --> boolean
# IsAtom(S) benar jika S adalah sebuah atom
def IsAtom(S):
    return type(S) != list

# IsList: list of list --> boolean
# IsList(S) benar jika S adalah sebuah list
def IsList(S):
    return type(S) == list


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def makePN(A, PN):
    return [A, PN]

# DEFINISI DAN SPESIFIKASI SELEKTOR
def AkarN(PN):
    return PN[0]

def Anak(PN):
    return PN[1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
def IsTreeNEmpty(PN):
    return PN == []

def IsOneElmtN(PN):
    return (IsTreeNEmpty(PN) == False) and (IsTreeNEmpty(Anak(PN)) == True)

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePB: integer, 2 PohonBiner --> PohonBiner
# MakePB(A, L, R) membuat Pohon Biner yang terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan
# REALISASI
def MakePB(A, L, R):
    return [A, L, R]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Akar: PohonBiner --> integer
# Akar(P) mengembalikan akar dari sebuah PohonBiner
# REALISASI
def Akar(P):
    return P[0]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Left: PohonBiner --> PohonBiner
# Left(P) mengembalikan subpohon kiri dari sebuah PohonBiner
# REALISASI
def Left(P):
    return P[1]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Right: PohonBiner --> PohonBiner
# Right(P) mengembalikan subpohon kanan dari sebuah PohonBiner
# REALISASI
def Right(P):
    return P[2]
\
# DEFINISI DAN SPESIFIKASI PREDIKAT
# DEFINISI DAN SPESIFIKASI
# IsTreeEmpty: T --> boolean
# IsTreeEmpty cek apakah Tree kosong
def IsTreeEmpty(T):
    return T == [] or T == None

# DEFINISI DAN SPESIFIKASI
# IsOneElmt: Binary Tree --> boolean
# IsOneElmt cek apakah Tree hanya satu elemen
def IsOneElmt(T):
    return IsTreeEmpty(Left(T)) and IsTreeEmpty(Right(T)) and not IsTreeEmpty(T)

# DEFINISI DAN SPESIFIKASI
# IsUnerLeft: Binary Tree --> boolean
# IsUnerLeft cek apakah sebuah tree Hanya mengandung sub pohon kiri
def IsUnerLeft(P):
    return not IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P))

# DEFINISI DAN SPESIFIKASI
# IsUnerRight: Binary Tree --> boolean
# IsUnerRight cek apakah sebuah tree hanya mengandung sub pohon kanan
def IsUnerRight(P):
    return IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))

# DEFINISI DAN SPESIFIKASI
# IsBiner: Binary Tree --> boolean
# IsBiner cek apakah Tree mengandung sub pohon kiri dan kanan
def IsBiner(P):
    return not IsTreeEmpty(Left(P)) and not IsTreeEmpty(Right(P))

# DEFINISI DAN SPESIFIKASI
# IsExistLeft: Binary Tree --> boolean
# IsExistLeft cek apakah Tree memiliki sub pohon kiri
def IsExistLeft(P):
    return IsBiner(P) or IsUnerLeft(P)
    
# # DEFINISI DAN SPESIFIKASI
# # IsExistRight: Binary Tree --> boolean
# # IsExistRight cek apakah Tree memiliki sub pohon kanan
def IsExistRight(P):
    return IsBiner(P) or IsUnerRight(P)

# DEFINISI DAN SPESIFIKASI SOAL NO 1
# FilterBilGen: List --> List
# FilterBilGen mengembalikan list yang berisi bilangan genap dari list L
def FilterBilGen(L):
    if IsTreeEmpty(L):
        return []
    else:
        if FirstElmt(L) % 2 == 0:
            return Konso(FirstElmt(L), FilterBilGen(Tail(L)))
        else:
            return FilterBilGen(Tail(L))
        
print(FilterBilGen([1,2,3,4,5,6,7,8,9,10]))
print(FilterBilGen([2,3,7,11,13,17,19,23]))

# DEFINISI DAN SPESIFIKASI SOAL NO 2
# IsContainList: List of List --> boolean
# IsContainList mengembalikan True jika dalam list terdapat list
def IsContaintList(L):
    if IsEmpty(L):
        return False
    else:
        if IsAtom(FirstList(L)):
            return IsContaintList(TailList(L))
        else:
            return True

print(IsContaintList([1,2,3,4,[5,6],7,8]))
print(IsContaintList([1,2,3,4,5,6,7,8]))

# DEFINISI DAN SPESIFIKASI SOAL NO 4
# SubListX: Tree NAry, Elemen --> list of Elemen
# SubListX mengembalikan list of elemen yang merupakan semua elemen yang berada di dalam tree yang memiliki akar X
def SubListXTree(P, X):
    if IsTreeNEmpty(P):
        return []
    elif AkarN(P) == X:
        return P
    else:
        return GetHelp(Anak(P), X)
    
def GetHelp(P, X):
    if IsTreeNEmpty(P):
        return []
    else:
        return SubListXTree(FirstList(P), X) + GetHelp(TailList(P), X)

def ToListBiasa(P):
    if IsEmpty(P):
        return []
    else:
        if IsAtom(FirstList(P)):
            return KonsLo(FirstList(P), ToListBiasa(TailList(P)))
        else:
            return ToListBiasa(FirstList(P)) + ToListBiasa(TailList(P))

def SubListX(P, X):
    return ToListBiasa(SubListXTree(P, X))

print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]), "Ridho"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Silvani"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Nuha"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Syahrafi"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Ega"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Noci"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Rendi"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Fikhrul"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Ruth"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Aji"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Eko"))
print(SubListX(makePN("Ridho",[makePN("Silvani",[makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])]),"Raffi"))

# DEFINISI DAN SPESIFIKASI SOAL NO 5
# IsMaxMod4: lambda, Binary Tree --> boolean
# IsMaxMod4 mengembalikan True jika elemen terbesar dari tree habis dibagi 4
def IsMaxMod4(f, P):
    if IsTreeEmpty(P):
        return False
    elif not IsExistRight(P):
        return f(Akar(P))
    else:
        return IsMaxMod4(f, Right(P))

print(IsMaxMod4(lambda x: x % 4 == 0, MakePB(40, [], [])))
print(IsMaxMod4(lambda x: x % 4 == 0,(MakePB(50, MakePB(35, [], []), MakePB(75, MakePB(60, [], []), MakePB(100, [], MakePB(120, [], [])))))))
print(IsMaxMod4(lambda x: x % 4 == 0,(MakePB(50, MakePB(35, [], []), MakePB(75, MakePB(60, [], []), MakePB(100, [], MakePB(120, [], MakePB(121, [], []))))))))

def IsOneElmtS(S):
    return len(S) == 1

def Max(S):
    if IsEmpty(S):
        return 0
    elif IsOneElmtS(S):
        if IsAtom(FirstList(S)):
            return FirstList(S)
        else:
            return Max(FirstList(S))
    else:
        if IsAtom(FirstList(S)):
            return max(FirstList(S), Max(TailList(S)))
        else:
            return max(Max(FirstList(S)), Max(TailList(S)))
        
print(Max([6, [7, 0, 9]]))

def AddX(P, X):
    if IsTreeEmpty(P):
        return MakePB(X, [], [])
    else:
        if X < Akar(P):
            return MakePB(Akar(P), AddX(Left(P), X), Right(P))
        else:
            return MakePB(Akar(P), Left(P), AddX(Right(P), X))

def Max(P):
    if IsOneElmt(P) or not IsExistRight(P):
        return Akar(P)
    else:
        return Max(Right(P))
        
def Min(P):
    if IsOneElmt(P) or not IsExistLeft(P):
        return Akar(P)
    else:
        return Min(Left(P))
        
def DelX(P, X):
    if IsTreeEmpty(P):
        return []
    elif Akar(P) > X:
        return MakePB(Akar(P), DelX(Left(P), X), Right(P))
    elif Akar(P) < X:
        return MakePB(Akar(P), Left(P), DelX(Right(P), X))
    elif Akar(P) == X:
        if IsOneElmt(P):
            return []
        else:
            if IsExistLeft(P):
                return MakePB(Max(Left(P)), DelX(Left(P), Max(Left(P))), Right(P))
            else:
                return MakePB(Min(Right(P)), Left(P), DelX(Right(P), Min(Right(P))))
        
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 85), 95), 100), 60), 120), 50))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 100))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 75))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 35))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 50))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 60))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 200))
print(DelX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 60))
print(DelX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 100))
print(DelX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 75))
print(DelX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 35))
print(DelX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 50))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120), 200), 25), 40), 50))

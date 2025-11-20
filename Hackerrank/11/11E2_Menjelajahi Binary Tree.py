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

# DEFINISI DAN SPESIFIKASI
# NBElmtTree: Binary Tree --> Integer
# NBElmtTree menghitung jumlah dari elemen Binary Tree
def NBElmtTree(T):
    if IsTreeEmpty(T):
        return 0
    else:
        if IsBiner(T):
            return 1 + NBElmtTree(Left(T)) + NBElmtTree(Right(T))
        elif IsUnerLeft(T):
            return 1 + NBElmtTree(Left(T))
        else:
            return 1 + NBElmtTree(Right(T))

# DEFINISI DAN SPESIFIKASI
# NBDaunTree: Binary Tree --> Integer
# NBDaunTree menghitung daun dari sebuah binary tree
def NBDaunTree(T):
    if IsTreeEmpty(T):
        return 0
    elif IsOneElmt(T):
        return 1
    else:
        if IsBiner(T):
            return NBElmtTree(Left(T)) + NBElmtTree(Right(T))
        elif IsUnerLeft(T):
            return NBElmtTree(Left(T))
        else:
            return NBElmtTree(Right(T))        

# DEFINISI DAN SPESIFIKASI
# IsMember: Binary Tree, integer --> boolean
# IsMember Mengecek apakah X ada di dalam Binary Tree
def IsMember(P, X):
    if IsTreeEmpty(P):
        return False
    elif Akar(P) == X:
        return True
    else:
        if IsBiner(P):
            return IsMember(Left(P), X) or IsMember(Right(P), X)
        elif IsUnerLeft(P):
            return IsMember(Left(P), X)
        else:
            return IsMember(Right(P), X) 

# DEFINISI DAN SPESIFIKASI
# IsSkewLeft: Binary Tree --> booelan
# IsSkewLeft Cek apakah Binary Tree hanya memiliki node kiri untuk setiap sub pohonya
def IsSkewLeft(P):
    if IsOneElmt(P):
        return True
    else:
        if IsUnerLeft(P):
            return IsSkewLeft(Left(P))
        else:
            return False

# DEFINISI DAN SPESIFIKASI
# IsSkewRight: Binary Tree --> booelan
# IsSkewRight Cek apakah Binary Tree hanya memiliki node kanan
def IsSkewRight(P):
    if IsOneElmt(P):
        return True
    else:
        if IsUnerRight(P):
            return IsSkewRight(Right(P))
        else:
            return False

# DEFINISI DAN SPESIFIKASI
# LevelOfX: Binary Tree, Integer --> Integer
# LevelOfX Mencari level dari X yang dijamin ada di dalam binary tree
def LevelOfX(P, X):
    if IsTreeEmpty(P):
        return 0
    elif Akar(P) == X:
        return 1
    else:
        if IsMember(Left(P), X):
            return 1 + LevelOfX(Left(P), X)
        else:
            return 1 + LevelOfX(Right(P), X)

# DEFINISI DAN SPESIFIKASI
# AddDaunTerkiri: Binary Tree, Integer --> Binary Tree
# AddDaunTerkiri Menambahkan daun terkiri dari Binary Tree
def AddDaunTerkiri(P, X):
    if IsTreeEmpty(P):
        return MakePB(X, [], [])
    elif Left(P) == []:
        return MakePB(Akar(P), MakePB(X, [], []), Right(P))
    else:
        return MakePB(Akar(P), AddDaunTerkiri(Left(P), X), Right(P))

# DEFINISI DAN SPESIFIKASI
# DelDaunTerkiri: Binary Tree --> Binary Tree
# DelDaunTerkiri Menghapus Daun Terkiri dari Binary Tree
def DelDaunTerkiri(P):
    if IsTreeEmpty(P) or IsOneElmt(P):
        return []
    else:
        if IsUnerRight(P):
            return MakePB(Akar(P), [], DelDaunTerkiri(Right(P)))
        else:
            return MakePB(Akar(P), DelDaunTerkiri(Left(P)), Right(P))
    
# DEFINISI DAN SPESIFIKASI
# DelDaun: Binary Tree --> Binary Tree
# DelDaun Menghapus Daun X dari Binary Tree jika ada
def DelDaun(P, X):
    if IsTreeEmpty(P) or IsOneElmt(P):
        return []
    elif  Akar(P) == X:
        return MakePB(Akar(P), Left(P), Right(P))
    else:
        if IsMember(Left(P), X):
            return MakePB(Akar(P), DelDaun(Left(P), X), Right(P))
        else:
            return MakePB(Akar(P), Left(P), DelDaun(Right(P), X))

# APLIKASI
print(NBElmtTree([]))
print(NBElmtTree(MakePB(10, MakePB(11, [], []), MakePB(12, [], []))))
print(NBDaunTree([]))
print(NBDaunTree(MakePB(10, MakePB(11, [], []), MakePB(12, [], []))))
print(IsMember(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 10))
print(IsMember(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 99))
print(IsMember(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 14))
print(IsMember(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 113))
print(IsMember(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 13))
print(IsSkewLeft(MakePB(10, MakePB(11, MakePB(12, MakePB(14, [], []), []), []), [])))
print(IsSkewLeft(MakePB(10, MakePB(11, MakePB(12, MakePB(14, [], MakePB(30, [], [])), []), []), [])))
print(IsSkewRight(MakePB(10, [], MakePB(11, [], MakePB(12, [], MakePB(14, [], []))))))
print(IsSkewRight(MakePB(10, MakePB(11, MakePB(12, MakePB(14, [], MakePB(30, [], [])), []), []), [])))
print(LevelOfX(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 16))
print(LevelOfX(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 14))
print(LevelOfX(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 10))
print(AddDaunTerkiri(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 110))
print(AddDaunTerkiri(AddDaunTerkiri(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 120), 300))
print(DelDaunTerkiri(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], []))))
print(DelDaunTerkiri(MakePB(10, MakePB(11, MakePB(12, MakePB(120, [], []), MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], []))))
print(DelDaunTerkiri(AddDaunTerkiri(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 120)))
print(DelDaun(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 5))
print(DelDaun(AddDaunTerkiri(MakePB(10, MakePB(11, MakePB(12, [], MakePB(13, MakePB(14, [], []), [])), MakePB(16, [], [])), MakePB(5, [], [])), 120), 13))
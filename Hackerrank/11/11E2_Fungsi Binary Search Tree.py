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
# AddX: Tree, integer --> BST
# AddX Menambahkan elemen x ke dalam Tree
def AddX(P, X):
    if IsTreeEmpty(P):
        return MakePB(X, [], [])
    else:
        if X < Akar(P):
            return MakePB(Akar(P), AddX(Left(P), X), Right(P))
        else:
            return MakePB(Akar(P), Left(P), AddX(Right(P), X))
   
def FindAkar(P):
    if not IsTreeEmpty(Left(P)):
        if IsExistRight(P):
            return Akar(Right(P))
        else:
            return Akar(Left(P))
    else:
        return Akar(P)

# DEFINISI DAN SPESIFIKASI
# DelX: BST, Integer --> BST
# DelX Menghapus ELemen X dari BST
def DelX(P, X):
    if IsTreeEmpty(P):
        return []
    elif X < Akar(P):
        return MakePB(Akar(P), DelX(Left(P), X), Right(P))
    elif X > Akar(P):
        return MakePB(Akar(P), Left(P), DelX(Right(P), X))
    elif X == Akar(P):
        if IsTreeEmpty(Left(P)) and IsTreeEmpty(Right(P)):
            return []
        elif IsUnerRight(P):
            return Right(P)
        elif IsUnerLeft(P):
            return Left(P)
        else:
            return MakePB(FindAkar(Left(P)), DelX(Left(P), FindAkar(Left(P))), DelX(Right(P), FindAkar(Left(P))))

# DEFINISI DAN SPESIFIKASI
# FindX: BST, integer --> integer
# FindX Mencari jarak dari akar sampai dengan x, x selalu ada di dalam tree
def FindX(P, x):
    if IsTreeEmpty(P) or Akar(P) == x:
        return 0
    else:
        if x < Akar(P):
            return 1 + FindX(Left(P), x)
        else:
            return 1 + FindX(Right(P), x)

print(AddX([], 50))
print(AddX(AddX([], 50), 75))
print(AddX(AddX(AddX([], 50), 75), 35))
print(AddX(AddX(AddX(AddX([], 50), 75), 35), 100))
print(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60))
print(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 75), 35), 100), 60), 120))
print(DelX(AddX(AddX(AddX(AddX(AddX(AddX([], 50), 35), 95), 100), 60), 120), 50))
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
print(FindX(MakePB(50, MakePB(35, [], []), MakePB(75, MakePB(60, [], []), MakePB(100, [], MakePB(120, [], [])))), 50))
print(FindX(MakePB(50, MakePB(35, [], []), MakePB(75, MakePB(60, [], []), MakePB(100, [], MakePB(120, [], [])))), 35))
print(FindX(MakePB(50, MakePB(35, [], []), MakePB(75, MakePB(60, [], []), MakePB(100, [], MakePB(120, [], [])))), 75))
print(FindX(MakePB(50, MakePB(35, [], []), MakePB(75, MakePB(60, [], []), MakePB(100, [], MakePB(120, [], [])))), 60))
print(FindX(MakePB(50, MakePB(35, [], []), MakePB(75, MakePB(60, [], []), MakePB(100, [], MakePB(120, [], [])))), 100))
print(FindX(MakePB(50, MakePB(35, [], []), MakePB(75, MakePB(60, [], []), MakePB(100, [], MakePB(120, [], [])))), 120))
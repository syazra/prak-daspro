# DEFINISI TYPE
# Type PohonBiner: <A: integer, L: PohonBiner, R: PohonBiner>
# Pohon Biner terdiri dari akar yang berupa elemen, 
# L dan R adalah Pohon Biner yang merupakan sub pohon kiri dan sub pohon kanan

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
# IsEmptyTree: PohonBiner --> boolean
# IsEmptyTree(P) mengecek apakah pohon biner P kosong atau bukan
# REALISASI
def IsEmptyTree(P):
    return P is None

# IsBiner: PohonBiner --> boolean
# IsBiner(P) memeriksa apakah subpohon P memiliki anak di kiri DAN kanan
def IsBiner(P):
    return not(IsEmptyTree(Left(P)) or IsEmptyTree(Right(P)))

# IsUnerLeft: PohonBiner --> boolean
# IsUnerLeft(P) memeriksa apakah subpohon P hanya memiliki anak di kiri
def IsUnerLeft(P):
    return not IsEmptyTree(Left(P)) and IsEmptyTree(Right(P))

# IsUnerRight: PohonBiner --> boolean
# IsUnerRight(P) memeriksa apakah subpohon P hanya memiliki anak di kanan
def IsUnerRight(P):
    return IsEmptyTree(Left(P)) and not IsEmptyTree(Right(P))

# IsDaun: PohonBiner --> boolean
# IsDaun(P) mengecek apakah subpohon biner berupa daun / memiliki 1 elemen saja
# REALISASI
def IsDaun(P):
    return IsEmptyTree(Left(P)) and IsEmptyTree(Right(P)) and not (IsEmptyTree(P))

def Plus(P):
    if IsEmptyTree(P):
        return 0
    else:
        if IsBiner(P):
            if Akar(Left(P)) < Akar(Right(P)):
                return Akar(Left(P)) + Plus(Left(P))
            else:
                return Akar(Right(P)) + Plus(Right(P))
        else:
            return 0
            
def Total(P):
    return Plus(P) + Akar(P)

def SurviveKah(X, P):
    if Total(P) < X:
        return 'Angjay B)'
    else:
        return 'Dead :skull:'

print(Total(MakePB(8, MakePB(9, None, None), None)))
print(Total(MakePB(4, MakePB(90, None, None), MakePB(10, MakePB(1, MakePB(8, None, None), MakePB(8, None, None)), MakePB(7, None, None)))))    
print(Total(MakePB(4, MakePB(8, MakePB(10, MakePB(6, None, None), None), MakePB(15, None, None)), MakePB(5, MakePB(18, None, None), MakePB(11, MakePB(11, None, None), MakePB(8, None, None))))))
print(Total(MakePB(7, MakePB(3, MakePB(1, None, None), MakePB(4, None, None)),MakePB(10, MakePB(9, None, None), MakePB(12, None, MakePB(14, None, None))))))
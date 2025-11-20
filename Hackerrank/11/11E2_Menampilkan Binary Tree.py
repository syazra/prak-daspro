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
# RepPrefix: Binary Tree --> List of List
# RepPrefix Mengubah struktur Binary Tree menjadi list of list
def RepPrefix(T):
    if IsTreeEmpty(T):
        return []
    else:
        return MakePB(Akar(T), RepPrefix(Left(T)), RepPrefix(Right(T)))

# DEFINISI DAN SPESIFIKASI
# MakeListDaun: Binary Tree --> List
# MakeListDaun Membuat List yang berisi elemen dari daun
def MakeListDaun(P):
    if IsTreeEmpty(P):
        return []
    elif IsOneElmt(P):
        return [Akar(P)]
    else:
        return MakeListDaun(Left(P)) + MakeListDaun(Right(P))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list --> list of list
# KonsLo(L, S) membentuk list baru dengan list (L) yang diberikan sebagai elemen pertama list of list (S)
def KonsLo(L, S):
    return [L] + S

# KonsLi: list of list, list --> list of list
# KonsLi(S, L) membentuk list baru dengan list (L) yang diberikan sebagai elemen terakhir list of list (S)
def KonsLi(S, L):
    return S + [L]

# DEFINISI DAN SPESIFIKASI
# MakeListPreOrder: Binary Tree --> List
# MakeListPreOrder Mencetak Tree dengan posisi elemen PreOrder
def MakeListPreOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        if IsBiner(P):
            return KonsLo(Akar(P), MakeListPreOrder(Left(P))) + MakeListPreOrder(Right(P))
        elif IsUnerLeft(P):
            return KonsLo(Akar(P), MakeListPreOrder(Left(P)))
        else:
            return KonsLo(Akar(P), MakeListPreOrder(Right(P)))
        
# DEFINISI DAN SPESIFIKASI
# MakeListInOrder: Binary Tree --> List
# MakeListInOrder Mencetak Tree dengan posisi elemen InOrder 
def MakeListInOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        if IsBiner(P):
            return KonsLi(MakeListInOrder(Left(P)), Akar(P)) + MakeListInOrder(Right(P))
        elif IsUnerLeft(P):
            return KonsLi(MakeListInOrder(Left(P)), Akar(P))
        else:
            return KonsLi(MakeListInOrder(Right(P)), Akar(P))

# DEFINISI DAN SPESIFIKASI
# MakeListPostOrder: Binary Tree --> List
# MakeListPostOrder Mencetak Tree dengan posisi elemen PostOrder 
def MakeListPostOrder(P):
    if IsTreeEmpty(P):
        return []
    else:
        if IsBiner(P):
            return MakeListPostOrder(Left(P)) + KonsLi(MakeListPostOrder(Right(P)), Akar(P))
        elif IsUnerLeft(P):
            return KonsLi(MakeListPostOrder(Left(P)), Akar(P))
        else:
            return KonsLi(MakeListPostOrder(Right(P)), Akar(P))

# APLIKASI
print(RepPrefix(MakePB('Saburo', MakePB('Rendi', MakePB('Ruth', [], []), MakePB('Aqila', MakePB('Syifa', [], []), MakePB('Eko', [], []))), MakePB('Rayhan', MakePB('Silvani', [], []), []))))
print(MakeListDaun(MakePB('Saburo', MakePB('Rendi', MakePB('Ruth', [], []), MakePB('Aqila', MakePB('Syifa', [], []), MakePB('Eko', [], []))), MakePB('Rayhan', MakePB('Silvani', [], []), []))))
print(MakeListPreOrder(MakePB('Saburo', MakePB('Rendi', MakePB('Ruth', [], []), MakePB('Aqila', MakePB('Syifa', [], []), MakePB('Eko', [], []))), MakePB('Rayhan', MakePB('Silvani', [], []), []))))
print(MakeListInOrder(MakePB('Saburo', MakePB('Rendi', MakePB('Ruth', [], []), MakePB('Aqila', MakePB('Syifa', [], []), MakePB('Eko', [], []))), MakePB('Rayhan', MakePB('Silvani', [], []), []))))
print(MakeListPostOrder(MakePB('Saburo', MakePB('Rendi', MakePB('Ruth', [], []), MakePB('Aqila', MakePB('Syifa', [], []), MakePB('Eko', [], []))), MakePB('Rayhan', MakePB('Silvani', [], []), []))))
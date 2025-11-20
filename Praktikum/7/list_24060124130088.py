# Nama File  : list_24060124130088.py
# Pembuat    : Syafira Azka Ramadhani
# Tanggal    : 29 Oktober 2024
# Deskripsi  : Berisi type dan operasi list

# DEFINISI DAN SPESIFIKASI TYPE
# ==============================
# Konstruktor menambahkan elemen di awal, notasi prefix
# type List: [] atau [e o List]
# Konstruktor menambahkan elemen di akhir, notasi postfix
# type List: [] atau [List o e]

# DEFINISI DAN SEPSIFIKASI KONSTRUKTOR
# =====================================
# Konso: elemen, List -> List
# Konso(e, L) menghasilkan sebuah List dari e dan L dengan e sebagai elemen pertama
# REALISASI
def Konso(e, L):
    return [e] + L

# Konsi: List, elemen -> List
# Konsi(L, e) menghasilkan sebuah List dari L dan e dengan e sebagai elemen terakhir
# REALISASI
def Konsi(L, e):
    return L + [e]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# ==================================
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) mengembalikan elemen pertama List L
# REALISASI
def FirstElmt(L):
    return L[0]

# Tail: List tidak kosong -> List
# Tail(L) mengembalikan List tanpa elemen pertama List L, mungkin kosong
# REALISASI
def Tail(L):
    return L[1:]

# LastElmt: List tidak kosong -> elemen
# LastElmt(L) mengembalikan elemen terakhir List L
# REALISASI
def LastElmt(L):
    return L[-1]

# Head: List tidak kosong -> List
# Head(L) mengembalikan List tanpa elemen terakhir List L, mungkin kosong
# REALISASI
def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# ==================================
# IsEmpty: List -> boolean
# IsEmpty(L) benar jika List L kosong
# REALISASI
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> boolean
# IsOneElmt(L) benar jika List L hanya mempunyai satu elemen
# REALISASI
def IsOneElmt(L):
    if IsEmpty(L):
        return False
    else:
        return Tail(L) == [] and Head(L) == []

# IsMember: elemen, List -> boolean
# IsMember(X, L) benar jika X adalah elemen dari list L
# REALISASI
def IsMember(X, L):
    if IsEmpty(L):
        return False
    else:
        return X == FirstElmt(L) or IsMember(X, Tail(L))

# IsPalindrom: List of character -> boolean
# IsPalindrom(L) benar jika L merupakan kata palindrom, yaitu kata yang sama jika dibaca dari kiri atau kanan
# REALISASI
def IsPalindrom(L):
    if IsEmpty(L) or IsOneElmt(L):
        return True
    else:
        return FirstElmt(L) == LastElmt(L) and IsPalindrom(Head(Tail(L)))

# DEFINISI DAN SPESIFIKASI OPERATOR
# ==================================
# NbElmt: List -> integer
# NbElmt(L) menghasilkan banyaknya elemen List L, nol jika kosong
# REALISASI
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

# ElmtkeN: integer > 0, List tidak kosong -> elemen
# ElmtkeN(N, L) mengirimkan elemen list yang ke N, N <= NbElmt(L) dan N > 0
# REALISASI
def ElmtkeN(N, L):
    if N == 1:
        return FirstElmt(L)
    else:
        return ElmtkeN(N - 1, Tail(L))

# Copy: List -> List
# Copy(L) menghasilkan list yang identik dengan list asal
# REALISASI
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), Copy(Tail(L)))

# Inverse: List -> List
# Inverse(L) menghasilkan list L yang dibalik, yaitu yang urutan elemennya adalah kebalikan dari list awal
# REALISASI
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(LastElmt(L), Inverse(Head(L)))

# Konkat: 2 List -> List
# Konkat(L1, L2) menghasilkan konkatenasi 2 buah list dengan list L2 "sesudah" list L1
# REALISASI
def Konkat(L1, L2):
    if IsEmpty(L2):
        return L1
    else:
        return Konsi(Konkat(L1, Head(L2)), LastElmt(L2))

# AddList: 2 List of integer -> List of integer
# AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah hasil penjumlahan
#   dari setiap elemen di L1 dan L2 pada posisi yang sama
# REALISASI
def AddList(L1, L2):
    if IsEmpty(L1) and IsEmpty(L2):
        return []
    elif IsEmpty(L1):
        return L2
    elif IsEmpty(L2):
        return L1
    else:
        return Konso(FirstElmt(L1) + FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlahan dari setiap elemen di list L
# REALISASI
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L) + SumElmt(Tail(L))

# AvgElmt: List of integer -> real
# AvgElmt(L) menghasilkan nilai rata-rata dari semua elemen di list L
# REALISASI
def AvgElmt(L):
    return SumElmt(L) / NbElmt(L)

# MaxElmt: List of integer -> elemen
# MaxElmt(L) mengembalikan elemen maksimum dari list L
# REALISASI
def MaxElmt(L):
    if IsOneElmt(L):
        return FirstElmt(L)
    elif FirstElmt(L) > LastElmt(L):
        return MaxElmt(Head(L))
    else:
        return MaxElmt(Tail(L))

# CountX: List of integer, integer -> integer
# CountX(L, X) menghitung banyaknya kemunculan dari bilangan X
# REALISASI  
def CountX(L, X):
    if IsEmpty(L):
        return 0
    else:
        if FirstElmt(L) == X:
            return 1 + CountX(Tail(L), X)
        else:
            return CountX(Tail(L), X)

# DEFINISI DAN SPESIFIKASI TYPE
# ==============================
# MakeMaxNBElmt: <Max: integer, CountMax: integer>
# <Max, CountMax> adalah tipe bentukan yang berisi Max sebagai bilangan maksimum
#   dan CountMax sebagai banyaknya kemunculan bilangan maksimum

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# =====================================
# MakeMaxNBElmt: 2 integer -> MaxNBElmt
# MakeMaxNBElmt(Max,CountMax) membentuk sebuah tipe bentukan yang berisi Max sebagai bilangan maksimum
#   dan CountMax sebagai banyaknya kemunculan bilangan maksimum
# REALISASI
def MakeMaxNBElmt(Max, CountMax):
    return [Max, CountMax]

# MaxNB: List of integer -> MaxNBElmt
# MaxNB(L) menghasilkan tipe bentukan yang berisi Max sebagai bilangan maksimum
#   dan CountMax sebagai banyaknya kemunculan bilangan maksimum
# REALISASI   
def MaxNB(L):
    return MakeMaxNBElmt(MaxElmt(L), CountX(L, MaxElmt(L)))

# APLIKASI
print(Konso(2, [3]))                             # --> [2, 3]
print(Konsi([3, 4, 5], 6))                       # --> [3, 4, 5, 6]
print(FirstElmt([3, 4, 5, 6, 7]))                # --> 3
print(Tail([3, 4, 5, 6, 7]))                     # --> [4, 5, 6, 7]
print(LastElmt([3, 4, 5, 6, 7]))                 # --> 7
print(Head([3, 4, 5, 6, 7]))                     # --> [3, 4, 5, 6]
print(IsEmpty([]))                               # --> True
print(IsEmpty([3, 4, 5, 6, 7]))                  # --> False
print(IsOneElmt([]))                             # --> False
print(IsOneElmt([3]))                            # --> True
print(IsMember(4, [3, 4, 5, 6, 7]))              # --> True
print(IsMember(14, [3, 4, 5, 6, 7]))             # --> False
print(IsPalindrom(['K', 'A', 'S', 'U', 'R']))    # --> False
print(IsPalindrom(['K', 'A', 'K', 'A', 'K']))    # --> True
print(NbElmt([3, 4, 5, 6, 7]))                   # --> 5
print(ElmtkeN(5, [3, 4, 5, 6, 7]))               # --> 7
print(Copy([]))                                  # --> []
print(Copy([3, 4, 5, 6, 7]))                     # --> [3, 4, 5, 6, 7]
print(Inverse([]))                               # --> []
print(Inverse([3, 4, 5, 6, 7]))                  # --> [7, 6, 5, 4, 3]
print(Konkat([], [4, 5, 6]))                     # --> [4, 5, 6]
print(Konkat([3, 4], []))                        # --> [3, 4]
print(Konkat([3, 4], [4, 5, 6]))                 # --> [3, 4, 4, 5, 6]
print(AddList([3, 4, 5], [6]))                   # --> [9, 4, 5]
print(AddList([3, 4], [4, 5, 6]))                # --> [7, 9, 6]
print(SumElmt([]))                               # --> 0
print(SumElmt([3, 4, 5, 6, 7]))                  # --> 25
print(AvgElmt([3, 4, 5, 6, 7]))                  # --> 5.0
print(MaxElmt([3, 4, 5, 6, 7]))                  # --> 7
print(MaxNB([3, 4, 5, 5, 6, 6, 7]))              # --> [7, 1]
print(MaxNB([3, 4, 7, 5, 7, 6, 7]))              # --> [7, 3]
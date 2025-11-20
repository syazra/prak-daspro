#--------------------------------- PREDIKAT ---------------------------------

# IsMember: elemen, List -> boolean
# IsMember(X, L) benar jika X adalah elemen dari List L
# REALISASI

# IsPalindrom: List of character -> boolean
# IsPalindrom(L) benar jika List L merupakan kata palindrom, yaitu kata yang sama jika dibaca dari kiri atau kanan
# REALISASI

#--------------------------------- OPERATOR --------------------------------- 

# ElmtkeN: integer ≥ 0, List -> elemen
# ElmtkeN(N, L) mengembalikan elemen ke-N dari List L
# REALISASI

# Copy: List -> List
# Copy(L) menghasilkan List L yang identik dengan List awal
# REALISASI

# Inverse: List -> List
# Inverse(L) menghasilkan List L yang dibalik, urutan elemen kebalikan dari List awal
# REALISASI

# Konkat: 2 List -> List
# Konkat(L1, L2) menghasilkan konkatenasi 2 buah List dengan List L2 "sesudah" List L1
# REALISASI

# AddList: 2 List of integer -> List of integer
# AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah hasil penjumlahan
# dari setiap elemen di L1 dan L2 pada posisi yang sama
# REALISASI

# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlah total dari semua elemen di List L
# REALISASI

# AvgElmt: List of integer -> real
# AvgElmt(L) menghasilkan nilai rata-rata dari semua elemen di List L
# REALISASI

# MaxElmt: List of integer -> integer
# MaxElmt(L) mengembalikan elemen maksimum dari List L
# REALISASI

# MaxNB: List of integer -> MaxNBElmt {<Max: integer, CountMax: integer ≥ 1>}
# MaxNB(L) menghasilkan tipe bentukan MaxNBElmt yang berisi Max sebagai bilangan maksimum
# dan CountMax sebagai banyaknya kemunculan bilangan maksimum
# REALISASI

# Nama File  : list_[nim].py
# Deskripsi  : Berisi type dan operasi list
# Pembuat    : 
# Tanggal    : 

# DEFINISI DAN SPESIFIKASI TYPE
# Konstruktor menambahkan elemen di awal, notasi prefix
# type List: [] atau [e o List]
# Konstruktor menambahkan elemen di akhir, notasi postfix
# type List: [] atau [List o e]

# DEFINISI DAN SEPSIFIKASI KONSTRUKTOR
# Konso: elemen, List -> List
# Konso(e, L) menghasilkan sebuah List dari e dan L dengan e sebagai elemen pertama
# REALISASI

# Konsi: List, elemen -> List
# Konsi(L, e) menghasilkan sebuah List dari L dan e dengan e sebagai elemen terakhir
# REALISASI

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) mengembalikan elemen pertama List L
# REALISASI

# Tail: List tidak kosong -> List
# Tail(L) mengembalikan List tanpa elemen pertama List L, mungkin kosong
# REALISASI

# LastElmt: List tidak kosong -> elemen
# LastElmt(L) mengembalikan elemen terakhir List L
# REALISASI

# Head: List tidak kosong -> List
# Head(L) mengembalikan List tanpa elemen terakhir List L, mungkin kosong
# REALISASI

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List -> boolean
# IsEmpty(L) benar jika List L kosong
# REALISASI

# IsOneElmt: List -> boolean
# IsOneElmt(L) benar jika List L hanya mempunyai satu elemen
# REALISASI

# IsMember: elemen, List -> boolean
# IsMember(X, L) benar jika X adalah elemen dari List L
# REALISASI

# IsPalindrom: List of character -> boolean
# IsPalindrom(L) benar jika List L merupakan kata palindrom, yaitu kata yang sama jika dibaca dari kiri atau kanan
# REALISASI

# DEFINISI DAN SPESIFIKASI OPERATOR
# NbElmt: List -> integer
# NbElmt(L) menghasilkan banyaknya elemen List L, nol jika kosong
# REALISASI

# ElmtkeN: integer ≥ 0, List -> elemen
# ElmtkeN(N, L) mengembalikan elemen ke-N dari List L
# REALISASI

# Copy: List -> List
# Copy(L) menghasilkan List L yang identik dengan List awal
# REALISASI

# Inverse: List -> List
# Inverse(L) menghasilkan List L yang dibalik, urutan elemen kebalikan dari List awal
# REALISASI

# Konkat: 2 List -> List
# Konkat(L1, L2) menghasilkan konkatenasi 2 buah List dengan List L2 "sesudah" List L1
# REALISASI

# AddList: 2 List of integer -> List of integer
# AddList(L1, L2) menghasilkan list baru yang setiap elemennya adalah hasil penjumlahan
# dari setiap elemen di L1 dan L2 pada posisi yang sama
# REALISASI

# SumElmt: List of integer -> integer
# SumElmt(L) menghasilkan jumlah total dari semua elemen di List L
# REALISASI

# AvgElmt: List of integer -> real
# AvgElmt(L) menghasilkan nilai rata-rata dari semua elemen di List L
# REALISASI

# MaxElmt: List of integer -> integer
# MaxElmt(L) mengembalikan elemen maksimum dari List L
# REALISASI

# MaxNB: List of integer -> MaxNBElmt {<Max: integer, CountMax: integer ≥ 1>}
# MaxNB(L) menghasilkan tipe bentukan MaxNBElmt yang berisi Max sebagai bilangan maksimum
# dan CountMax sebagai banyaknya kemunculan bilangan maksimum
# REALISASI


# Nama file  : typepecahan.py
# Pembuat    : Syafira Azka Ramadhani
# Tanggal    : 29 September 2024
# Deskripsi  : Membuat type bentukan pecahan beserta konstruktor, selektor, operator, dan predikatnya


# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type pecahan: <n: integer>=0, d: integer>0>
# <n: integer>=0, d: integer>0> n adalah pembilang (numerator) dan d adalah penyebut (denumerator), dengan penyebut sebuah pecahan tidak boleh nol

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeP: integer>=0, integer>0 --> pecahan
# MakeP(n,d) membentuk sebuah pecahan dari pembilang n dan penyebut d, dengan n dan d merupakan bilangan integer
# REALISASI
def MakeP(n,d):
    return [n,d]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Pemb: pecahan --> integer>=0
# Pemb(P) memberikan numerator pembilang n dari pecahan P
# REALISASI
def Pemb(P):
    return P[0]

# Peny: pecahan --> integer>0
# Peny(P) memberikan denumerator penyebut d dari pecahan P
# REALISASI
def Peny(P):
    return P[1]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI OPERATOR
# AddP: 2 pecahan --> pecahan
# AddP(P1,P2) menambahkan dua buah pecahan P1 dan P2: (n1/d1)+(n2/d2) = (n1*d2+n2*d1)/d1*d2
# REALISASI
def AddP(P1,P2):
    return MakeP((Pemb(P1)*Peny(P2)+Pemb(P2)*Peny(P1)),(Peny(P1)*Peny(P2)))

# SubP: 2 pecahan --> pecahan
# SubP(P1,P2) mengurangkan dua buah pecahan P1 dan P2: (n1/d1)-(n2/d2) = (n1*d2-n2*d1)/d1*d2
# REALISASI
def SubP(P1,P2):
    return MakeP((Pemb(P1)*Peny(P2)-Pemb(P2)*Peny(P1)),(Peny(P1)*Peny(P2)))

# MulP: 2 pecahan --> pecahan
# MulP(P1,P2) mengalikan dua buah pecahan P1 dan P2: (n1/d1)*(n2/d2) = (n1*n2)/(d1*d2)
# REALISASI
def MulP(P1,P2):
    return MakeP((Pemb(P1)*Pemb(P2)),(Peny(P1)*Peny(P2)))

# DivP: 2 pecahan --> pecahan
# DivP(P1,P2) membagi dua buah pecahan P1 dan P2: (n1/d1)/(n2/d2) = (n1*d2)/(d1*n2)
# REALISASI
def DivP(P1,P2):
    return MakeP(Pemb(P1)*Peny(P2),(Peny(P1)*Peny(P2)))

# RealP: pecahan --> real
# Reap(P) menuliskan bilangan pecahan dalam notasi desimal
# REALISASI
def RealP(P):
    return Pemb(P)/Peny(P)

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqP: 2 pecahan --> boolean
# IsEqP(P1,P2) true jika P1 = P2, membandingkan apakah dua buah pecahan sama nilainya: n1/d1 = n2/d2 jika dan hanya jika n1*d2 = n2*d1
# REALISASI
def IsEqP(P1,P2):
    return Pemb(P1)*Peny(P2) == Peny(P1)*Pemb(P2)

# IsLtP: 2 pecahan --> boolean
# IsLtP(P1,P2) true jika P1 < P2, membandingkan dua buah pecahan apakah P1 lebih kecil nilainya dari P2: n1/d1 < n2/d2 jika dan hanya jika n1*d2 < n2*d1
# REALISASI
def IsLtP(P1,P2):
    return Pemb(P1)*Peny(P2) < Peny(P1)*Pemb(P2)

# IsGtP: 2 pecahan --> boolean
# IsGtP(P1,P2) true jika P1 > P2, membandingkan nilai dua buah pecahan, apakah P1 lebih besar nilainya dari P2: n1/d1 > n2/d2 jika dan hanya jika n1*d2 > n2*d1
# REALISASI
def IsGtP(P1,P2):
    return Pemb(P1)*Peny(P2) > Peny(P1)*Pemb(P2)

# ===========================================================================================================================

# APLIKASI
print(AddP(MakeP(-5,10),MakeP(10,7)))
print(SubP(MakeP(1,2),MakeP(3,4)))
print(MulP(MakeP(-1,9),MakeP(0,4)))
print(DivP(MakeP(-9,2),MakeP(3,1)))
print(RealP(MakeP(1,1)))
print(IsEqP(MakeP(1,9),(2,18)))
print(IsLtP(MakeP(1,99),(1,98)))
print(IsGtP(MakeP(1,99),(-1,98)))
# Pembuat    : Syafira Azka Ramadhani
# Tanggal    : 21 Oktober 2024
# Deskripsi  : Membuat tipe bentukan pecahan campuran beserta selektor, konstruktor, operator, dan predikatnya

# ======================================================================================================================
# TYPE PECAHAN CAMPURAN
# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type pecahan: <n: integer, d: integer>0>
#   {<n,d> adalah pecahan dengan n sebagai pembilang (numerator) dan d sebagai penyebut (denumerator)}

# type pecahanc: <bil: integer, n: integer, d: integer>0>
#   {<bil,n,d> adalah pecahan campuran dengan bil sebagai bilangan bulat pecahan, n sebagai pembilang (numerator),
# d sebagai penyebut (denumerator), dan pembilang selalu lebih kecil dari penyebut (n < d)}

# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# pemb: pecahan --> integer
#   {pemb(P) memberikan pembilang (numerator) n dari pecahan P}
# REALISASI
def pemb(P):
    return P[0]

# peny: pecahan --> integer>0
#   {peny(P) memberikan penyebut (denumerator) d dari pecahan P}
# REALISASI
def peny(P):
    return P[1]

# bilangan: pecahanc --> integer
#   {bilangan(PC) memberikan bilangan bulat pecahan bil dari pecahan campuran PC}
# REALISASI
def bilangan(PC):
    return PC[0]

# num: pecahanc --> integer
#   {num(PC) memberikan pembilang (numerator) n dari pecahan campuran PC}
# REALISASI
def num(PC):
    return PC[1]

# denum: pecahanc --> integer>0
#   {denum(PC) memberikan penyebut (denumerator) d dari pecahan campuran PC}
# REALISASI
def denum(PC):
    return PC[2]

# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeP: integer, integer>0 --> pecahan
#   {MakeP(n,d) membentuk sebuah pecahan dari pembilang (numerator) n dan penyebut (denumerator) d}
# REALISASI
def MakeP(n,d):
    return [n,d]

# MakePC: 2 integer, integer>0 --> pecahanc
#   {MakePC(bil,n,d) membentuk sebuah pecahan campuran dari bilangan bulat pecahan bil, pembilang (numerator) n,
# dan penyebut (denumerator) d}
# REALISASI
def MakePC(bil,n,d):
    return [bil,n,d]

# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI OPERATOR
# KonversiPecahan: pecahanc --> pecahan
#   {KonversiPecahan(P) mengubah pecahan campuran P menjadi tipe pecahan biasa}
# REALISASI
def KonversiPecahan(P):
    if bilangan(P) < 0:
        return MakeP(bilangan(P)*denum(P)-num(P), denum(P))
    else:
        return MakeP(bilangan(P)*denum(P)+num(P), denum(P))

# KonversiReal: pecahanc --> real
#   {KonversiReal(P) mengubah pecahan campuran P menjadi nilai real}
# REALISASI
def KonversiReal(P):
    if bilangan(P) < 0:
        return (bilangan(P)*denum(P)-num(P))/denum(P)
    else:
        return (bilangan(P)*denum(P)+num(P))/denum(P)

# Add: pecahanc --> pecahan
#   {Add(P1,P2) menjumlahkan pecahan campuran P1 dan P2 dengan hasil dalam bentuk pecahan biasa}
# REALISASI
def Add(P1,P2):
    return MakeP(pemb(KonversiPecahan(P1))*peny(KonversiPecahan(P2))+pemb(KonversiPecahan(P2))*
            peny(KonversiPecahan(P1)), peny(KonversiPecahan(P1))*peny(KonversiPecahan(P2)))

# AddP: pecahan --> pecahanc
#   {AddP(P1,P2) mengembalikan hasil penjumlahan pecahan campuran P1 dan P2 ke dalam bentuk pecahan campuran}
# REALISASI
def AddP(P1,P2):
    if pemb(Add(P1,P2)) < 0:
        if abs(pemb(Add(P1,P2)))//peny(Add(P1,P2)) == 0:
            return MakePC(0, pemb(Add(P1,P2)), peny(Add(P1,P2)))
        else:
            return MakePC(-(abs(pemb(Add(P1,P2)))//peny(Add(P1,P2))), abs(pemb(Add(P1,P2)))%peny(Add(P1,P2)),
                    peny(Add(P1,P2)))
    else:
        return MakePC(pemb(Add(P1,P2))//peny(Add(P1,P2)), pemb(Add(P1,P2))%peny(Add(P1,P2)), peny(Add(P1,P2)))

# Sub: pecahanc --> pecahan
#   {Sub(P1,P2) mengurangkan pecahan campuran P1 dan P2 dengan hasil dalam bentuk pecahan biasa}
# REALISASI
def Sub(P1,P2):
    return MakeP(pemb(KonversiPecahan(P1))*peny(KonversiPecahan(P2))-pemb(KonversiPecahan(P2))*
            peny(KonversiPecahan(P1)), peny(KonversiPecahan(P1))*peny(KonversiPecahan(P2)))

# SubP: pecahan --> pecahanc
#   {SubP(P1,P2) mengembalikan hasil pengurangan pecahan campuran P1 dan P2 ke dalam bentuk pecahan campuran}
# REALISASI
def SubP(P1,P2):
    if pemb(Sub(P1,P2)) < 0:
        if abs(pemb(Sub(P1,P2)))//peny(Sub(P1,P2)) == 0:
            return MakePC(0, pemb(Sub(P1,P2)), peny(Sub(P1,P2)))
        else:
            return MakePC(-(abs(pemb(Sub(P1,P2)))//peny(Sub(P1,P2))), abs(pemb(Sub(P1,P2)))%peny(Sub(P1,P2)),
                    peny(Sub(P1,P2)))
    else:
        return MakePC(pemb(Sub(P1,P2))//peny(Sub(P1,P2)), pemb(Sub(P1,P2))%peny(Sub(P1,P2)), peny(Sub(P1,P2)))

# Div: pecahanc --> pecahan
#   {Div(P1,P2) membagi pecahan campuran P1 dan P2 dengan hasil dalam bentuk pecahan biasa}
# REALISASI
def Div(P1,P2):
    return MakeP(pemb(KonversiPecahan(P1))*peny(KonversiPecahan(P2)), peny(KonversiPecahan(P1))*
            pemb(KonversiPecahan(P2)))

# DivP: pecahan --> pecahanc
#   {DivP(P1,P2) mengembalikan hasil pembagian pecahan campuran P1 dan P2 ke dalam bentuk pecahan campuran}
# REALISASI
def DivP(P1,P2):
    if (pemb(Div(P1,P2)) < 0 and peny(Div(P1,P2)) >=0) or (pemb(Div(P1,P2)) >= 0 and peny(Div(P1,P2)) < 0):
        if abs(pemb(Div(P1,P2)))//abs(peny(Div(P1,P2))) == 0:
            return MakePC(0, -abs(pemb(Div(P1,P2))), abs(peny(Div(P1,P2))))
        else:
            return MakePC(-(abs(pemb(Div(P1,P2)))//abs(peny(Div(P1,P2)))), abs(pemb(Div(P1,P2)))%abs(peny(Div(P1,P2))),
                    abs(peny(Div(P1,P2))))
    else:
        return MakePC(abs(pemb(Div(P1,P2)))//abs(peny(Div(P1,P2))), abs(pemb(Div(P1,P2)))%abs(peny(Div(P1,P2))),
                abs(peny(Div(P1,P2))))

# Mul: pecahanc --> pecahan
#   {Mul(P1,P2) mengalikan pecahan campuran P1 dan P2 dengan hasil dalam bentuk pecahan biasa}
# REALISASI
def Mul(P1,P2):
    return MakeP(pemb(KonversiPecahan(P1))*pemb(KonversiPecahan(P2)), peny(KonversiPecahan(P1))*
            peny(KonversiPecahan(P2)))

# MulP: pecahan --> pecahanc
#   {MulP(P1,P2) mengembalikan hasil perkalian pecahan campuran P1 dan P2 ke dalam bentuk pecahan campuran}
# REALISASI
def MulP(P1,P2):
    if pemb(Mul(P1,P2)) < 0:
        if abs(pemb(Mul(P1,P2)))//peny(Mul(P1,P2)) == 0:
            return MakePC(0, pemb(Mul(P1,P2)), peny(Mul(P1,P2)))
        else:
            return MakePC(-(abs(pemb(Mul(P1,P2)))//peny(Mul(P1,P2))), abs(pemb(Mul(P1,P2)))%peny(Mul(P1,P2)),
                    peny(Mul(P1,P2)))
    else:
        return MakePC(pemb(Mul(P1,P2))//peny(Mul(P1,P2)), pemb(Mul(P1,P2))%peny(Mul(P1,P2)), peny(Mul(P1,P2)))

# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqP: 2 pecahanc --> boolean
#   {IsEqP(P1,P2) benar jika P1 = P2, membandingkan apakah P1 sama dengan P2}
# REALISASI
def IsEqP(P1,P2):
    return KonversiReal(P1) == KonversiReal(P2)

# IsLtP: 2 pecahanc --> boolean
#   {IsLtP(P1,P2) benar jika P1 < P2, membandingkan apakah P1 lebih kecil dari P2}
# REALISASI
def IsLtP(P1,P2):
    return KonversiReal(P1) < KonversiReal(P2)

# IsGtP: 2 pecahanc --> boolean
#   {IsGtP(P1,P2) benar jika P1 > P2, membandingkan apakah P1 lebih besar dari P2}
# REALISASI
def IsGtP(P1,P2):
    return KonversiReal(P1) > KonversiReal(P2)

# ======================================================================================================================

# APLIKASI
print(KonversiPecahan(MakePC(0,-1,42)))      # --> [-1, 42]
print(KonversiPecahan(MakePC(-5,1,7)))       # --> [-36, 7]
print(KonversiPecahan(MakePC(0,3,4)))        # --> [3, 4]
print(KonversiPecahan(MakePC(-7,0,2)))       # --> [-14, 2]
print(KonversiReal(MakePC(2,8,32)))          # --> 2.25
print(KonversiReal(MakePC(-16,3,4)))         # --> -16.75
print(KonversiReal(MakePC(0,-1,8)))          # --> -0.125
print(KonversiReal(MakePC(0,0,2)))           # --> 0.0
print(AddP(MakePC(2,1,2), MakePC(-2,3,4)))   # --> [0, -2, 8]
print(AddP(MakePC(2,3,5), MakePC(-1,5,6)))   # --> [0, 23, 30]
print(AddP(MakePC(1,1,2), MakePC(0,1,2)))    # --> [2, 0, 4]
print(AddP(MakePC(1,1,2), MakePC(-8,0,9)))   # --> [-6, 9, 18]
print(SubP(MakePC(3,1,2), MakePC(-2,3,4)))   # --> [6, 2, 8]
print(SubP(MakePC(0,-1,3), MakePC(0,2,3)))   # --> [-1, 0, 9]
print(SubP(MakePC(-4,2,3), MakePC(-4,1,2)))  # --> [0, -1, 6]
print(SubP(MakePC(9,1,2), MakePC(9,1,2)))    # --> [0, 0, 4]
print(DivP(MakePC(9,2,4), MakePC(-1,0,2)))   # --> [-9, 4, 8]
print(DivP(MakePC(-5,1,2), MakePC(-5,1,2)))  # --> [1, 0, 22]
print(DivP(MakePC(3,1,3), MakePC(-3,3,4)))   # --> [0, -40, 45]
print(DivP(MakePC(-9,2,5), MakePC(2,1,5)))   # --> [-4, 15, 55]
print(MulP(MakePC(-1,0,2), MakePC(-6,1,5)))  # --> [6, 2, 10]
print(MulP(MakePC(2,0,2), MakePC(-4,1,7)))   # --> [-8, 4, 14]
print(MulP(MakePC(0,-1,4), MakePC(0,2,4)))   # --> [0, -2, 16]
print(MulP(MakePC(0,1,9), MakePC(0,3,7)))    # --> [0, 3, 63]
print(IsEqP(MakePC(9,0,2), MakePC(18,0,4)))  # --> False
print(IsEqP(MakePC(-2,1,2), MakePC(-2,2,4))) # --> True
print(IsEqP(MakePC(0,-1,2), MakePC(-1,0,2))) # --> False
print(IsEqP(MakePC(5,0,1), MakePC(5,0,9)))   # --> True
print(IsLtP(MakePC(0,6,8), MakePC(0,2,5)))   # --> False
print(IsLtP(MakePC(0,-4,9), MakePC(0,-1,3))) # --> True
print(IsLtP(MakePC(-1,0,7), MakePC(-1,2,4))) # --> False
print(IsLtP(MakePC(0,-1,9), MakePC(0,-1,6))) # --> False
print(IsGtP(MakePC(0,-1,2), MakePC(-2,0,1))) # --> True
print(IsGtP(MakePC(2,0,8), MakePC(2,2,4)))   # --> False
print(IsGtP(MakePC(8,0,1), MakePC(7,3,4)))   # --> True
print(IsGtP(MakePC(-2,0,9), MakePC(-2,2,4))) # --> True

########################################################################################################################

# Pembuat    : Syafira Azka Ramadhani
# Tanggal    : 21 Oktober 2024
# Deskripsi  : Membuat tipe bentukan garis beserta selektor, konstruktor, operator, dan predikatnya

# ======================================================================================================================
# TYPE GARIS
# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type point: <x: integer, y: integer>
#   {<x,y> adalah sebuah point dengan x sebagai absis dan y sebagai ordinat}

# type garis: <P1: point, P2: point>
#   {<P1,P2> adalah sebuah garis dengan P1 sebagai titik awal dan P2 sebagai titik akhir}

# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# absis: point --> integer
#   {absis(P) memberikan absis x dari point P}
# REALISASI
def absis(P):
    return P[0]

# ordinat: point --> integer
#   {ordinat(P) memberikan ordinat y dari point P}
# REALISASI
def ordinat(P):
    return P[1]

# titikAwal: garis --> point
#   {titikAwal(G) memberikan point P1 dari garis G}
# REALISASI
def titikAwal(G):
    return G[0]

# titikAkhir: garis --> point
#   {titikAkhir(G) memberikan point P2 dari garis G}
# REALISASI
def titikAkhir(G):
    return G[1]

# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2 integer --> point
#   {MakePoint(x,y) membentuk sebuah point dengan absis x dan ordinat y}
# REALISASI
def MakePoint(x,y):
    return [x,y]

# MakeGaris: 2 point --> garis
#   {MakeGaris(P1,P2) membentuk sebuah garis dengan titik awal P1 dan titik akhir P2}
# REALISASI
def MakeGaris(P1,P2):
    return [P1,P2]

# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI OPERATOR
# Gradien: garis --> real
#   {Gradien(G) menghitung gradien garis G}
# REALISASI
def Gradien(G):
    if (absis(titikAkhir(G))-absis(titikAwal(G))) == 0:
        return 0.0
    else:
        return (ordinat(titikAkhir(G))-ordinat(titikAwal(G)))/(absis(titikAkhir(G))-absis(titikAwal(G)))

# PanjangGaris: garis --> real
#   {PanjangGaris(G) menghitung panjang garis G}
# REALISASI
def PanjangGaris(G):
    return ((absis(titikAkhir(G))-absis(titikAwal(G)))**2+(ordinat(titikAkhir(G))-ordinat(titikAwal(G)))**2)**0.5

# ======================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSejajar: 2 garis --> boolean
#   {IsSejajar(G1,G2) benar jika G1 sejajar dengan G2 (gradien G1 sama dengan gradien G2)}
# REALISASI
def IsSejajar(G1,G2):
    return Gradien(G1) == Gradien(G2)

# IsTegakLurus: 2 garis --> boolean
#   {IsTegakLurus(G1,G2) benar jika G1 tegak lulus dengan G2 (gradien G1 dikali gradien G2 sama dengan -1)}
# REALISASI
def IsTegakLurus(G1,G2):
    if (absis(titikAkhir(G1))-absis(titikAwal(G1))) == 0 or (absis(titikAkhir(G2))-absis(titikAwal(G2))) == 0:
        return (absis(titikAkhir(G1))-absis(titikAwal(G1))) != 0 or (absis(titikAkhir(G2))-absis(titikAwal(G2))) != 0
    else:
        return Gradien(G1)*Gradien(G2) == -1

# ======================================================================================================================

# APLIKASI
print(Gradien(MakeGaris(MakePoint(6,3), MakePoint(8,-2))))                                                  # --> -2.5
print(Gradien(MakeGaris(MakePoint(1,-2), MakePoint(1,1))))                                                  # --> 0.0
print(Gradien(MakeGaris(MakePoint(5,0), MakePoint(0,10))))                                                  # --> -2.0
print(Gradien(MakeGaris(MakePoint(9,0), MakePoint(-1,-7))))                                                 # --> 0.7
print(PanjangGaris(MakeGaris(MakePoint(1,3), MakePoint(5,6))))                                              # --> 5.0
print(PanjangGaris(MakeGaris(MakePoint(9,2), MakePoint(1,2))))                                              # --> 8.0
print(PanjangGaris(MakeGaris(MakePoint(0,0), MakePoint(0,10))))                                             # --> 10.0
print(PanjangGaris(MakeGaris(MakePoint(1,5), MakePoint(1,20))))                                             # --> 15.0
print(IsSejajar(MakeGaris(MakePoint(-2,2), MakePoint(2,-2)), MakeGaris(MakePoint(2,2), MakePoint(-2,-2))))  # --> False
print(IsSejajar(MakeGaris(MakePoint(1,4), MakePoint(1,0)), MakeGaris(MakePoint(5,2), MakePoint(5,8))))      # --> True
print(IsSejajar(MakeGaris(MakePoint(6,6), MakePoint(2,0)), MakeGaris(MakePoint(8,6), MakePoint(6,2))))      # --> False
print(IsSejajar(MakeGaris(MakePoint(5,1), MakePoint(2,3)), MakeGaris(MakePoint(6,2), MakePoint(9,0))))      # --> True
print(IsTegakLurus(MakeGaris(MakePoint(6,6), MakePoint(2,6)), MakeGaris(MakePoint(8,4), MakePoint(8,6))))   # --> True
print(IsTegakLurus(MakeGaris(MakePoint(2,2), MakePoint(4,5)), MakeGaris(MakePoint(6,2), MakePoint(9,0))))   # --> True
print(IsTegakLurus(MakeGaris(MakePoint(0,0), MakePoint(-2,0)), MakeGaris(MakePoint(3,2), MakePoint(3,-3)))) # --> True
print(IsTegakLurus(MakeGaris(MakePoint(7,0), MakePoint(-1,0)), MakeGaris(MakePoint(5,5), MakePoint(-5,5)))) # --> False
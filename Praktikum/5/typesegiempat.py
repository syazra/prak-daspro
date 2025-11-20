# Nama file  : typesegiempat.py
# Pembuat    : Syafira Azka Ramadhani
# Tanggal    : 29 September 2024
# Deskripsi  : Membuat tipe bentukan segiempat, garis, dan point beserta konstruktor, selektor, operator, dan predikatnya


# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type point: <x: real, y: real>
# <x: real, y: real> adalah sebuah point dengan x adalah absis dan y adalah ordinat

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makePoint: 2 real --> point
# makePoint(x,y) membentuk sebuah point dengan x adalah absis dan y adalah ordinat
# REALISASI
def makePoint(x,y):
    return [x,y]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# absis: point --> real
# absis(P) memberikan absis dari point P
# REALISASI
def absis(P):
    return P[0]

# ordinat: point --> real
# ordinat(P) memberikan ordinat dari point P
# REALISASI
def ordinat(P):
    return P[1]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type garis: <P1: point, P2: point>
# <P1: point, P2: point> adalah sebuah garis dengan titik awal P1 dan titik akhir P2

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makeGaris: 2 point --> garis
# makeGaris(P1,P2) membentuk sebuah garis dengan titik awal P1 dan titik akhir P2
# REALISASI
def makeGaris(P1,P2):
    return [P1,P2]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# titikAwal: garis --> point
# titikAwal(G) memberikan point P1 dari garis G
# RELISASI
def titikAwal(G):
    return G[0]

# titikAkhir: garis --> point
# titikAkhir(G) memberikan point P2 dari garis G
# REALISASI
def titikAkhir(G):
    return G[1]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type segiempat: <G1: garis, G2: garis, G3: garis, G4: garis>
# <G1: garis, G2: garis, G3: garis, G4: garis> adalah sebuah segiempat yang dibentuk dari 4 buah garis

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makeSegiEmpat: 4 garis --> segiempat
# makeSegiEmpat(G1,G2,G3,G4) membentuk sebuah segi empat dengan menggunakan 4 garis
# REALISASI
def makeSegiEmpat(G1,G2,G3,G4):
    return [G1,G2,G3,G4]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# garis1: segiempat --> garis
# garis1(S) memberikan garis G1 dari segiempat S
# RELISASI
def garis1(S):
    return S[0]

# garis2: segiempat --> garis
# garis2(S) memberikan garis G2 dari segiempat S
# RELISASI
def garis2(S):
    return S[1]

# garis3: segiempat --> garis
# garis3(S) memberikan garis G3 dari segiempat S
# RELISASI
def garis3(S):
    return S[2]

# garis4: segiempat --> garis
# garis4(S) memberikan garis G4 dari segiempat S
# RELISASI
def garis4(S):
    return S[3]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI OPERATOR
# panjangGaris: garis --> real
# panjangGaris(G) menghitung panjang dari sebuah garis
# REALISASI
def panjangGaris(G):
    return ((absis(titikAkhir(G))-absis(titikAwal(G)))**2 + (ordinat(titikAkhir(G))-ordinat(titikAwal(G)))**2)**0.5

# gradien: garis --> real
# gradien(G) menghitung gradien dari sebuah garis dengan rumus matematis y2-y1/x2-x1
# REALISASI
def gradien(G):
    if (absis(titikAkhir(G))-absis(titikAwal(G))) == 0:
        return 0.0
    else:
        return (ordinat(titikAkhir(G))-ordinat(titikAwal(G)))/(absis(titikAkhir(G))-absis(titikAwal(G)))

# AreaBujurSangkar: segiempat --> real
# AreaBujurSangkar(S) menghitung luas dari bujur sangkar, tetapi apabila bukan bujur sangkar mengeluarkan bilangan real berupa 0.0
# REALISASI
def AreaBujurSangkar(S):
    if isBujurSangkar(S):
        return (panjangGaris(garis1(S)) * panjangGaris(garis2(S)))
    else:
        return 0.0

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT
# isTegakLurus: 2 garis --> boolean
# isTegakLurus(G1,G2) true jika kedua garis saling tegak lurus, membandingkan apakah kedua garis saling tegak lurus menggunakan rumus gradien
# REALISASI
def isTegakLurus(G1,G2):
    if (absis(titikAkhir(G1))-absis(titikAwal(G1))) == 0 or (absis(titikAkhir(G2))-absis(titikAwal(G2))) == 0:
        return (absis(titikAkhir(G1))-absis(titikAwal(G1))) != 0 or (absis(titikAkhir(G2))-absis(titikAwal(G2))) != 0
    else:
        return ((ordinat(titikAkhir(G1))-ordinat(titikAwal(G1)))/(absis(titikAkhir(G1))-absis(titikAwal(G1))) * (absis(titikAkhir(G2))-absis(titikAwal(G2)))/(absis(titikAkhir(G2))-absis(titikAwal(G2)))) == -1

# isBujurSangkar: segiempat --> boolean
# isBujurSangkar(S) true jika semua garis sama panjang dan memiliki garis yang saling tegak lurus
# REALISASI
def isBujurSangkar(S):
    return (panjangGaris(garis1(S)) == panjangGaris(garis2(S)) == panjangGaris(garis3(S)) == panjangGaris(garis4(S))) and isTegakLurus(garis1(S),garis2(S))

# isJajarGenjang: segiempat --> boolean
# isJajarGenjang(S) true jika 2 pasang garis yang berhadapan memiliki gradien yang sama, tetapi 2 garis yang berpotongan memiliki gradien tidak sama dengan -1
# REALISASI    
def isJajarGenjang(S):
    if gradien(garis1(S)) == gradien(garis2(S)) and gradien(garis3(S)) == gradien(garis4(S)):
        return gradien(garis1(S)) != gradien(garis3(S)) and gradien(garis1(S)) * gradien(garis3(S)) != -1
    elif gradien(garis1(S)) == gradien(garis4(S)) and gradien(garis2(S)) == gradien(garis3(S)):
        return gradien(garis1(S)) != gradien(garis2(S)) and gradien(garis1(S)) * gradien(garis2(S)) != -1
    elif gradien(garis1(S)) == gradien(garis3(S)) and gradien(garis2(S)) == gradien(garis4(S)):
        return gradien(garis1(S)) != gradien(garis2(S)) and gradien(garis1(S)) * gradien(garis2(S)) != -1
    else:
        return False

# ===========================================================================================================================
 
# APLIKASI
# print(isBujurSangkar(makeSegiEmpat(makeGaris(makePoint(-3.0,-2.0),makePoint(-1.0,-4.0)),makeGaris(makePoint(-1.0,-4.0),makePoint(-3.0,-6.0)),makeGaris(makePoint(-3.0,-6.0),makePoint(-5.0,-4.0)),makeGaris(makePoint(-5.0,-4.0),makePoint(-3.0,-2.0)))))
# print(isBujurSangkar(makeSegiEmpat(makeGaris(makePoint(0.0,-1.0),makePoint(-1.0,0.0)),makeGaris(makePoint(-1.0,0.0),makePoint(-2.0,-1.0)),makeGaris(makePoint(-2.0,-1.0),makePoint(-1.0,-2.0)),makeGaris(makePoint(-1.0,-2.0),makePoint(0.0,-1.0)))))
# print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(8.1,2.1),makePoint(8.1,9.1)),makeGaris(makePoint(1.1,4.1),makePoint(1.1,-3.1)),makeGaris(makePoint(1.1,-3.1),makePoint(8.1,2.1)),makeGaris(makePoint(1.1,4.1),makePoint(8.1,9.1)))))
# print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(1.0,2.0),makePoint(4.0,2.0)),makeGaris(makePoint(6.0,4.0),makePoint(4.0,2.0)),makeGaris(makePoint(1.0,2.0),makePoint(3.0,4.0)),makeGaris(makePoint(3.0,4.0),makePoint(6.0,4.0)))))
# print(AreaBujurSangkar(makeSegiEmpat(makeGaris(makePoint(-3.0,-2.0),makePoint(-1.0,-4.0)),makeGaris(makePoint(-1.0,-4.0),makePoint(-3.0,-6.0)),makeGaris(makePoint(-3.0,-6.0),makePoint(-5.0,-4.0)),makeGaris(makePoint(-5.0,-4.0),makePoint(-3.0,-2.0)))))
# print(AreaBujurSangkar(makeSegiEmpat(makeGaris(makePoint(1.0,9.5),makePoint(0.0,-9.5)),makeGaris(makePoint(0.0,-9.5),makePoint(0.5,5.0)),makeGaris(makePoint(0.5,5.0),makePoint(4.9,5.2)),makeGaris(makePoint(4.9,5.2),makePoint(1.0,9.5)))))
# print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(1.0,5.0),makePoint(5.0,5.0)),makeGaris(makePoint(5.0,5.0),makePoint(9.0,9.0)),makeGaris(makePoint(9.0,9.0),makePoint(4.0,9.0)),makeGaris(makePoint(4.0,9.0),makePoint(1.0,5.0)))))
# print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(5.0,5.0),makePoint(5.0,9.0)),makeGaris(makePoint(5.0,9.0),makePoint(0.0,7.0)),makeGaris(makePoint(0.0,7.0),makePoint(0.0,3.0)),makeGaris(makePoint(0.0,3.0),makePoint(5.0,5.0)))))
# print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(2.0, 4.0), makePoint(6.0, 4.0)), makeGaris(makePoint(6.0, 6.0), makePoint(2.0, 6.0)), makeGaris(makePoint(2.0, 4.0), makePoint(2.0, 6.0)), makeGaris(makePoint(6.0, 4.0), makePoint(6.0, 6.0)))))
print(isJajarGenjang(makeSegiEmpat(
    makeGaris(makePoint(1.0,1.0), makePoint(3.0,1.0)),
    makeGaris(makePoint(3.0,1.0), makePoint(3.0,3.0)),
    makeGaris(makePoint(3.0,3.0), makePoint(1.0,3.0)),
    makeGaris(makePoint(1.0,3.0), makePoint(1.0,1.0))
))
)
print(isJajarGenjang(makeSegiEmpat(
    makeGaris(makePoint(0.0,0.0), makePoint(8.0,0.0)),
    makeGaris(makePoint(8.0,0.0), makePoint(10.0,3.0)),
    makeGaris(makePoint(10.0,3.0), makePoint(2.0,3.0)),
    makeGaris(makePoint(2.0,3.0), makePoint(0.0,0.0))
))
)
print(isJajarGenjang(makeSegiEmpat(
    makeGaris(makePoint(0.0,0.0), makePoint(4.0,0.0)),
    makeGaris(makePoint(4.0,0.0), makePoint(4.0,4.0)),
    makeGaris(makePoint(4.0,4.0), makePoint(0.0,4.0)),
    makeGaris(makePoint(0.0,4.0), makePoint(0.0,0.0))
))
)
print(isJajarGenjang(makeSegiEmpat(
    makeGaris(makePoint(1.0,1.0), makePoint(6.0,1.0)),
    makeGaris(makePoint(6.0,1.0), makePoint(6.0,3.0)),
    makeGaris(makePoint(6.0,3.0), makePoint(1.0,3.0)),
    makeGaris(makePoint(1.0,3.0), makePoint(1.0,1.0))
))
)

isJajarGenjang(makeSegiEmpat(
    makeGaris(makePoint(5.0, 5.0), makePoint(5.0, 9.0)),
    makeGaris(makePoint(5.0, 9.0), makePoint(0.0, 7.0)),
    makeGaris(makePoint(0.0, 7.0), makePoint(0.0, 3.0)),
    makeGaris(makePoint(0.0, 3.0), makePoint(5.0, 5.0))
))
print(isJajarGenjang(makeSegiEmpat(
        makeGaris(makePoint(0.0, 0.0), makePoint(2.0, 3.0)),
        makeGaris(makePoint(2.0, 3.0), makePoint(4.0, 0.0)),
        makeGaris(makePoint(4.0, 0.0), makePoint(2.0, -3.0)),
        makeGaris(makePoint(2.0, -3.0), makePoint(0.0, 0.0))
)))

isJajarGenjang(makeSquare(makeGaris(makePoint(5.0, 5.0), makePoint(5.0, 9.0)), makeGaris(makePoint(5.0, 9.0), makePoint(0.0, 7.0)), makeGaris(makePoint(0.0, 7.0), makePoint(0.0, 3.0)),
makeGaris(makePoint(0.0, 3.0), makePoint(5.0, 5.0))
    ))
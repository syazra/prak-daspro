# Nama file  : typegaris.py
# Pembuat    : Syafira Azka Ramadhani
# Tanggal    : 29 September 2024
# Deskripsi  : Membuat type bentukan point dan garis beserta konstruktor, selektor, operator, dan predikatnya


# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type point: <x: integer, y: integer>
# <x: integer, y: integer> adalah sebuah point dengan x adalah absis dan y adalah ordinat

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# makePoint: 2 integer --> point
# makePoint(x,y) membentuk sebuah point dengan x adalah absis dan y adalah ordinat
# REALISASI
def makePoint(x,y):
    return [x,y]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# absis: point --> integer
# absis(P) memberikan absis dari point P
# REALISASI
def absis(P):
    return P[0]

# ordinat: point --> integer
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

# DEFINISI DAN SPESIFIKASI OPERATOR
# panjangGaris: garis --> real
# panjangGaris(G) menghitung panjang dari garis G
# REALISASI
def panjangGaris(G):
    return ((absis(titikAkhir(G))-absis(titikAwal(G)))**2 + (ordinat(titikAkhir(G))-ordinat(titikAwal(G)))**2)**0.5

# gradien: garis --> real
# gradien(G) menghitung gradien dari sebuah garis dengan rumus matematis y2-y1/x2-x1
# REALISASI
def gradien(G):
    return (ordinat(titikAkhir(G))-ordinat(titikAwal(G)))/(absis(titikAkhir(G))-absis(titikAwal(G)))

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT
# isSejajar: 2 garis --> boolean
# isSejajar(G1,G2) true jika gradien G1 = gradien G2, membandingkan apakah gradien G1 = gradien G2
# REALISASI
def isSejajar(G1,G2):
    return gradien(G1) == gradien(G2)

# ===========================================================================================================================

# APLIKASI
print(isSejajar(makeGaris(makePoint(1,2),makePoint(3,4)),makeGaris(makePoint(2,3),makePoint(3,4))))
print(panjangGaris(makeGaris(makePoint(1,3),makePoint(9,-2))))
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

def istegak(G1, G2):
    return (absis(titikAwal(G1)) == absis(titikAkhir(G1)) and ordinat(titikAwal(G2)) == ordinat(titikAkhir(G2))
            or absis(titikAwal(G2)) == absis(titikAkhir(G2)) and ordinat(titikAwal(G1)) == ordinat(titikAkhir(G1)))
    
def gradien(G):
    if (absis(titikAkhir(G)) - absis(titikAwal(G))) == 0.0:
        return -1.0
    else:
        return (ordinat(titikAkhir(G))-ordinat(titikAwal(G)))/(absis(titikAkhir(G))-absis(titikAwal(G)))

def tegak(G1, G2):
    if (gradien(G1) == -1.0 and gradien(G2) == 0.0) or (gradien(G2) == -1.0 and gradien(G1) == 0.0):
        return True
    else:
        return gradien(G1) * gradien(G2) == -1

print(istegak([[0, 2],[0,-2]], [[2, 0], [-2, 0]]))
print(tegak([[0, 2],[0,-2]], [[2, 0], [-2, 0]]))
print(istegak([[0, 2],[0,-2]], [[0, 2],[0,-2]]))
print(tegak([[0, 2],[0,-2]], [[0, 2],[0,-2]]))
print(istegak([[0, 0],[2,2]], [[0, 2],[2,0]]))
print(tegak([[0, 0],[2,2]], [[0, 2],[2,0]]))
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Point: 2 integer --> point
# Point(x,y) adalah sebuat point dimana x adalah absis dan y adalah ordinat
# REALISASI
def makePoint(x,y):
    return [x,y]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Absis: point --> integer
# Absis(P) mengembalikan absis Point P
# REALISASI
def X(P):
    return P[0]

# Ordinat: point --> integer
# Ordinat(P) mengembalikan ordinat Point P
# REALISASI
def Y(P):
    return P[1]

print(X(makePoint(1,2)))
# # DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# # makeBalok: 3 real --> balok
# # makeBalok(p,l,t) membentuk sebuah balok dengan panjang p, lebar l, dan tinggi t.
# # REALISASI
# def makeBalok(p,l,t):
#     return [p,l,t]
    
# # DEFINISI DAN SPESIFIKASI SELEKTOR
# # P: balok ---> real
# # P(B) mengembalikan nilai panjang p dari balok B.
# # REALISASI
# def P(B):
#     return B[0]
    
# # L: balok ---> real
# # L(B) mengembalikan nilai lebar l dari balok B.
# # REALISASI
# def L(B):
#     return B[1]
    
# # T: balok ---> real
# # T(B) mengembalikan nilai tinggi t dari balok B.
# # REALISASI
# def T(B):
#     return B[2]

# def IsKubus(B):
#     return P(B)==L(B)==T(B)

# def Luas(B):
#     return (2*P(B)*L(B))+(2*P(B)*(T(B)))+(2*L(B)*T(B))

# def Volume(B):
#     return P(B)*L(B)*T(B)

# def D_R(B):
#     return round((P(B)**2+L(B)**2+T(B)**2)**0.5, 5)

# print(IsKubus(makeBalok(1, 4, 10)))
# print(Luas(makeBalok(1, 4, 10)))
# print(Volume(makeBalok(1, 4, 10)))
# print(D_R(makeBalok(1, 4, 10)))

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Point: 2 integer --> point
# Point(x,y) adalah sebuat point dimana x adalah absis dan y adalah ordinat
# REALISASI
def makePoint(x,y):
    return [x,y]

# makeKaret: point, real --> karet
# makeKaret(P,r) membentuk sebuah karet tidak putus dari titik pusat P dan jari-jari r.
# REALISASI
def makeKaret(P,r):
    return [P,r]

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

# MidPoint: karet ---> point
# MidPoint(K) mengembalikan titik pusat (x,y) dari karet K
# REALISASI
def MidPoint(K):
    return K[0]

# JariJari: karet ---> real
# JariJari(K) mengembalikan jari-jari r dari karet K
# REALISASI
def JariJari(K):
    return K[1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSinggung: 2 karet ---> boolean
# IsSinggung(K1,K2) bernilai true apabila karet K1 dan karet K2 besinggungan tepat hanya pada 1 titik.
# REALISASI
# (((X(MidPoint(K2))-X(MidPoint(K1)))**2)+((Y(MidPoint(K2))-Y(MidPoint(K1)))**2))**0.5 == (JariJari(K1)+JariJari(K2) or abs(JariJari(K1)-JariJari(K2)))

def IsSinggung(K1,K2):
    return ((((X(MidPoint(K2))-X(MidPoint(K1)))**2)+((Y(MidPoint(K2))-Y(MidPoint(K1)))**2))**0.5 == JariJari(K1)+JariJari(K2)) or ((((X(MidPoint(K2))-X(MidPoint(K1)))**2)+((Y(MidPoint(K2))-Y(MidPoint(K1)))**2))**0.5 == abs(JariJari(K1)-JariJari(K2)))
            
# IsPotongX: karet ---> boolean
# IsPotongX(K) bernilai true apabila karet K berpotongan atau bersinggungan setidaknya di 1 titik dengan sumbu X.
# REALISASI
def IsPotongX(K):
    return abs(Y(MidPoint(K))) <= JariJari(K)

# IsPotongY: karet ---> boolean
# IsPotongY(K) bernilai true apabila karet K berpotongan atau bersinggungan setidaknya di 1 titik dengan sumbu Y
# REALISASI
def IsPotongY(K):
    return abs(X(MidPoint(K))) <= JariJari(K)

print(IsSinggung(makeKaret(makePoint(0, 8), 10), makeKaret(makePoint(4, 5), 5)))
print(IsPotongX(makeKaret(makePoint(-1, 11), 7)))
print(IsPotongY(makeKaret(makePoint(1, 0), 3)))
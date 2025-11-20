#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, Set -> Set
# Konso(e,S) menghasilkan sebuah Set dari e dan S dengan e sebagai elemen pertama
# Realisasi
def Konso(e,S):
    return [e] + S

# Konsi: Set, elemen -> Set
# Konsi(S,e) menghasilkan sebuah Set dari S dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(S,e):
    return S + [e]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: Set tidak kosong -> elemen
# FirstElmt(S) menghasilkan elemen pertama Set S
# Realisasi
def FirstElmt(S):
    return S[0]

# LastElmt: Set tidak kosong -> elemen
# LastElmt(S) menghasilkan elemen terakhir Set S
# Realisasi
def LastElmt(S):
    return S[-1]

# Tail: Set tidak kosong -> Set
# Tail(S) menghasilkan Set tanpa elemen pertama Set S, mungkin kosong
# Realisasi
def Tail(S):
    return S[1:]

# Head: Set tidak kosong -> Set
# Head(S) menghasilkan Set tanpa elemen terakhir Set S, mungkin kosong
# Realisasi
def Head(S):
    return S[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: Set -> Boolean
# IsEmpty(S) true jika Set kosong
# Realisasi
def IsEmpty(S):
    return S == []

# IsOneElmt: Set -> Boolean
# IsOneElmt(S) true jika Set hanya satu elemen
# Realisasi
def IsOneElemt(S):
    if IsEmpty(S):
        return False
    else :
        return Tail(S)==[] and Head(S)==[]

def IsMember(x, L):
    if IsEmpty(L):
        return False
    else:
        return IsMember(x, Tail(L)) or FirstElmt(L) == x

def Rember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == x:
            return Tail(L)
        else:
            return Konso(FirstElmt(L), Rember(x, Tail(L)))

def Nilai2(S1, S2):
    if IsEmpty(S1):
        return 0
    else:
        if IsMember(FirstElmt(S1), S2):
            if IsMember(FirstElmt(S2), S1):
                return Nilai2(Rember(FirstElmt(S2), S1), Tail(S2))
            else:
                return 2 + Nilai2(Tail(S1), Rember(FirstElmt(S1), Tail(S2)))
        else:
            return 1 + Nilai2(Tail(S1), Tail(S2))

def NbElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return 1 + NbElmt(Tail(L))

def Hasil(S1, S2):
    if IsEmpty(S1):
        return 0
    elif IsEmpty(S2):
        return NbElmt(S1)
    else:
        if IsMember(FirstElmt(S1), S2) and FirstElmt(S1) != FirstElmt(S2):
            return 2 + Hasil(Tail(S1), Rember(FirstElmt(S1), S2))
        elif FirstElmt(S1) == FirstElmt(S2):
            return Hasil(Tail(S1), Tail(S2))
        else:
            return 1 + Hasil(Tail(S1), Tail(S2))
        
print(Hasil([3,2,7,78,60,47,87,4,5,1,100,1001,0,99], [2,5,60,3,4,0]))
print(Hasil([2,5,60,3,4,0], [3,2,7,78,60,47,87,4,5,1,100,1001,0,99]))
print(Nilai2([1,2,3, 4, 5, 6,7,8,9,10],[8,9,10,11,12,13,14,1,2]))
print(Nilai2([8,9,10,11,12,13,14,1,2], [1,2,3, 4, 5, 6,7,8,9,10]))
print(Nilai2([2, 3, 4],[-9,1,2,3,4,5,6,7,8]))
print(Hasil([-9,1,2,3,4,5,6,7,8], [2, 3, 4]))

# def Pirate(S1, S2):
#     if Nilai2(S1, S2) < Nilai2(S2, S1):
#         return 'UpsideDownUmbrella'
#     elif Nilai2(S1, S2) == Nilai2(S2, S1):
#         return 'WhiteCanvas dan UpsideDownUmbrella Bersatu, Perdamaian adalah Keuntungan Tak Terhingga umat manusia! (Apasih B1, susah amat)!'
#     else:
#         return 'WhiteCanvasUmbrella'
    
# print(Pirate([1,2,3, 4, 5, 6,7,8,9,10],[8,9,10,11,12,13,14,1,2]))
# print(Nilai2([2,5,60,3,4,0], [3,2,7,78,60,47,87,4,5,1,100,1001,0,99]))
# print(Pirate([2, 3, 4],[-9,1,2,3,4,5,6,7,8]))
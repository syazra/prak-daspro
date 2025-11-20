# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# make_makhlukmagis: 4 int --> makhlukmagis
# make_makhlukmagis(HP, Attack,Stamina, Defense) membentuk sebuah tipe data mystical_beast dengan atribut HP , Attack, Stamina, dan Defense
def make_makhlukmagis(HP, Attack, Stamina, Defense):
    return [HP, Attack, Stamina, Defense]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# HP(M) :  makhlukmagis --> integer
# HP(M) mengambil nilai HP pada makhluk magis M
def HP(M):
    return M[0]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Attack(M) : makhlukmagis --> integer
# Attack(M) mengambil nilai Attack pada makhluk magis M
def Attack(M):
    return M[1]
    
# DEFINISI DAN SPESIFIKASI SELEKTOR
# Stamina(M) : makhlukmagis --> integer
# Stamina(M) mengambil nilai Stamina pada makhluk magis M
def Stamina(M):
    return M[2]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Defense(M) : makhlukmagis --> integer
# Defense(M) mengambil nilai Defense pada makhluk magis M
def Defense(M):
    return M[3]

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# Konso: elemen, list -> List
# Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# Realisasi
def Konso(e,L):
    return [e] + L

# Konsi: List, elemen -> List
# Konsi(L,e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# Realisasi
def Konsi(L,e):
    return L + [e]

#DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong -> elemen
# FirstElmt(L) menghasilkan elemen pertama list L
# Realisasi
def FirstElmt(L):
    return L[0]

# LastElmt: List tidak kosong -> elemen
# LastElmt(L) menghasilkan elemen terakhir list L
# Realisasi
def LastElmt(L):
    return L[-1]

# Tail: List tidak kosong -> List
# Tail(L) menghasilkan list tanpa elemen pertama list L, mungkin kosong
# Realisasi
def Tail(L):
    return L[1:]

# Head: List tidak kosong -> List
# Head(L) menghasilkan list tanpa elemen terakhir list L, mungkin kosong
# Realisasi
def Head(L):
    return L[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEmpty: List -> Boolean
# IsEmpty(L) true jika list kosong
# Realisasi
def IsEmpty(L):
    return L == []

# IsOneElmt: List -> Boolean
# IsOneElmt(L) true jika list hanya satu elemen
# Realisasi
def IsOneElemt(L):
    if IsEmpty(L):
        return False
    else :
        return Tail(L)==[] and Head(L)==[]

def CP_Multiplier(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(0.5 * (Stamina(FirstElmt(L)) + (Defense(FirstElmt(L)) + HP(FirstElmt(L))) + Attack(FirstElmt(L))**2), CP_Multiplier(Tail(L)))

def Power(L):
    if IsEmpty(L):
        return []
    else:
        return Konso((Attack(FirstElmt(L)) * Defense(FirstElmt(L)) ** 0.5 * FirstElmt(CP_Multiplier(L))) / 10, Power(Tail(L)))
    
def Champion(L1,L2):
    if IsEmpty(Power(L1)):
        return L2
    elif IsEmpty(Power(L2)):
        return L1
    elif FirstElmt(Power(L1)) == FirstElmt(Power(L2)):
        return Champion(Tail(L1),Tail(L2))
    elif FirstElmt(Power(L1)) > FirstElmt(Power(L2)):
        return Konso(FirstElmt(L1), Champion(Tail(L1),Tail(L2)))
    else:
        return Konso(FirstElmt(L2), Champion(Tail(L1),Tail(L2)))
    
print(Champion([make_makhlukmagis(100, 40, 45, 50), make_makhlukmagis(75, 25, 35, 40)], [make_makhlukmagis(95, 35, 40, 45), make_makhlukmagis(70, 20, 30, 35), make_makhlukmagis(65, 10, 25, 35), make_makhlukmagis(80, 20, 40, 50), make_makhlukmagis(110, 50, 55, 60), make_makhlukmagis(105, 45, 50, 55), make_makhlukmagis(85, 30, 35, 40), make_makhlukmagis(90, 35, 50, 55), make_makhlukmagis(77, 28, 32, 37), make_makhlukmagis(88, 33, 38, 42)]))
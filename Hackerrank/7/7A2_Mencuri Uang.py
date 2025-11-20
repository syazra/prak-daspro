# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
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

# VERSI 1
string = 'Inv35t4s1'
List = list(string)

def hitung_angka(List):
    if List == '':
        return 0
    elif FirstElmt(List) >= '0' and FirstElmt(List) <= '9':
        return int(FirstElmt(List)) + hitung_angka(Tail(List))
    else:
        return hitung_angka(Tail(List))

print(f"{hitung_angka(string)} Milyar")


# VERSI 2
def ToList(L):
    return list(L)

def ToInteger(L):
    if IsEmpty(L):
        return 0
    elif (FirstElmt(L) == '1' or FirstElmt(L) == '2' or FirstElmt(L) == '3' or FirstElmt(L) == '4' or FirstElmt(L) == '5'
          or FirstElmt(L) == '6' or FirstElmt(L) == '7' or FirstElmt(L) == '8' or FirstElmt(L) == '9') :
        return int(FirstElmt(L)) + ToInteger(Tail(L))
    else:
        return ToInteger(Tail(L))
    
def Hasil(L):
    return str(ToInteger(ToList(L))) + ' Milyar'

print(ToInteger(['I', 'n', 'v', '3', '5', 't', '4', 's', '1']))
print(Hasil('Inv35t4s1'))
# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list --> list of list
# KonsLo(L, S) membentuk list baru dengan list (L) yang diberikan sebagai elemen pertama list of list (S)
def KonsLo(L, S):
    return [L] + S

# KonsLi: list of list, list --> list of list
# KonsLi(S, L) membentuk list baru dengan list (L) yang diberikan sebagai elemen terakhir list of list (S)
def KonsLi(S, L):
    return S + [L]

#====================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: list of list tidak kosong --> list
# FirstList(S) menghasilkan elemen pertama list of list S, mungkin sebuah list atau atom
def FirstList(S):
    return S[0]

# TailList: list of list tidak kosong --> list of list
# TailList(S) menghasilkan "sisa" list of list S tanpa elemen pertamanya
def TailList(S):
    return S[1:]

# LastList: list of list tidak kosong --> list
# LastList(S) menghasilkan elemen terakhir list of list S, mungkin sebuah list atau atom
def LastList(S):
    return S[-1]

# HeadList: list of list tidak kosong --> list of list
# HeadList(S) menghasilkan "sisa" list of list S tanpa elemen terakhirnya
def HeadList(S):
    return S[:-1]

#====================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST
# IsAtom: list of list --> boolean
# IsAtom(S) benar jika S adalah sebuah atom
def IsAtom(S):
    return type(S) != list

# IsList: list of list --> boolean
# IsList(S) benar jika S adalah sebuah list
def IsList(S):
    return type(S) == list

# IsEmpty: list of list --> boolean
# IsEmpty(S) benar jika S adalah list of list kosong
def IsEmpty(S):
    return S == []

# IsOneElmt: list of list --> boolean
# IsOneElmt(S) benar jika S hanya memiliki satu elemen
def IsOneElmt(S):
    if IsEmpty(S):
        return False
    else:
        return TailList(S) == [] and HeadList(S) == []

def ToList(L):
    if IsEmpty(L):
        return []
    else:
        if IsAtom(FirstList(L)):
            return KonsLo(FirstList(L), ToList(TailList(L)))
        else:
            return ToList(FirstList(L)) + ToList(TailList(L))

def Pangkat(L):
    if IsOneElmt(L):
        return 0
    else:
        return 1 + Pangkat(TailList(L))
    
def TranslateBinary(L):
    if IsEmpty(L):
        return 0
    elif FirstList(L) == 0:
        return TranslateBinary(TailList(L))
    else:
        return FirstList(L) * 2 ** Pangkat(L) + TranslateBinary(TailList(L))
    
def IsDiserang(L):
    if TranslateBinary(ToList(L)) == 0 or TranslateBinary(ToList(L)) % 2 != 0:
        return 'santai dulu ga sih'
    else:
        return 'ril ges no fek'
    
print(IsDiserang([[0],[1, [[[0, 0]]]]]))


# DEFINISI DAN SEPSIFIKASI KONSTRUKTOR
# Konso: elemen, List --> List
# Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
# REALISASI
def Konso(e,L):
    return [e] + L

# Konsi: List, elemen --> List
# Konsi(L,e) menghasilkan sebuah list dari L dan e dengan e sebagai elemen terakhir
# REALISASI
def Konsi(L,e):
    return L + [e]

#=================================================================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List tidak kosong --> elemen
# FirstElmt(L) mengembalikan elemen pertama list L
# REALISASI
def FirstElmt(L):
    return L[0]

# Tail: List tidak kosong --> List
# Tail(L) mengembalikan list tanpa elemen pertama list L, mungkin kosong
# REALISASI
def Tail(L):
    return L[1:] 

# LastElmt: List tidak kososng --> elemen
# LastElmt(L) mengembalikan elemen terakhir pada list L
# REALISASI
def LastElmt(L):
    return L[-1]

# Head: List tidak kosong --> List
# Head(L) mengembalikan list tanpa elemen terakhir list L, mungkin kosong
# REALISASI
def Head(L):
    return L[:-1]

def EvaluateExpression(L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L) == '+':
            return FirstElmt(Tail(L)) + FirstElmt(Tail(Tail(L)))
        elif FirstElmt(L) == '-':
            return FirstElmt(Tail(L)) - FirstElmt(Tail(Tail(L)))
        elif FirstElmt(L) == "*":
            return FirstElmt(Tail(L)) * FirstElmt(Tail(Tail(L)))
        else:
            return FirstElmt(Tail(L)) / FirstElmt(Tail(Tail(L)))
        
print(EvaluateExpression(['+', 10, 4]))

def kurang(L):
    return FirstElmt(L) - FirstElmt(Tail(L))

# MaxElmt: List of integer --> integer
# MaxElmt(L) mengembalikan elemen maksimum dari list L
# REALISASI
def Kurang(L):
    if IsEmpty(L) or IsEmpty(Tail(L)):
        return 0
    else:
        return max(FirstElmt(Tail(L)) - FirstElmt(L), Kurang(Tail(L)))
        

# ElmtkeN: integer > 0, List tidak kosong --> elemen
# ElmtkeN(N,L) mengirimkan elemen list yang ke N, N <= NbElmt(L) dan N > 0
# REALISASI
def ElmtkeN(N, L):
    if N == 1:
        return FirstElmt(L)
    else:
        return ElmtkeN(N-1,Tail(L))
      
def BestDayInvest(L, a, b):
    if IsEmpty(L):
        return 0
    elif Kurang(L) < 0:
        return 'Mending turu'
    elif ElmtkeN(b, L) - ElmtkeN(b-1, L)  == Kurang(L):
        return 'Hari ke ' + str(b-1)
    else:
        return BestDayInvest(L, a, b-1)

print(Kurang([0.46,0.31,0.21,0.12,0.11,0.07]))
print(BestDayInvest([0.46,0.41,0.54,0.62,0.03,0.07,0.54, 0.20], 1, 8))
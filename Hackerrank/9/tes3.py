# Nama File : ArusPenata.py
# Pembuat   : 
# Tanggal   :

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list -> list of list
# KonsLo(L, S) membentuk list baru dengan list (L) yang diberikan sebagai elemen pertama list of list (S)
# REALISASI
def KonsLo(L, S):
    return [L] + S

# KonsLi: list of list, list -> list of list
# KonsLi(S, L) membentuk list baru dengan list (L) yang diberikan sebagai elemen terakhir list of list (S)
# REALISASI
def KonsLi(S, L):
    return S + [L]
 
# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: list of list tidak kosong -> list
# FirstList(S) menghasilkan elemen pertama list of list S, mungkin sebuah list atau atom
# REALISASI
def FirstList(S):
    return S[0]

# TailList: list of list tidak kosong -> list of list
# TailList(S) menghasilkan "sisa" list of list S tanpa elemen pertamanya
# REALISASI
def TailList(S):
    return S[1:]

# LastList: list of list tidak kosong -> list
# LastList(S) menghasilkan elemen terakhir list of list S, mungkin sebuah list atau atom
# REALISASI
def LastList(S):
    return S[-1]

# HeadList: list of list tidak kosong -> list of list
# HeadList(S) menghasilkan "sisa" list of list S tanpa elemen terakhirnya
# REALISASI
def HeadList(S):
    return S[:-1]
  
# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST
# IsAtom: list of list -> boolean
# IsAtom(S) benar jika S adalah sebuah atom
# REALISASI
def IsAtom(S):
    return type(S) != list

# IsList: list of list -> boolean
# IsList(S) benar jika S adalah sebuah list
# REALISASI
def IsList(S):
    return type(S) == list

# IsEmpty: list of list -> boolean
# IsEmpty(S) benar jika S adalah list of list kosong
# REALISASI
def IsEmpty(S):
    return S == []

def IsOneElmt(S):
    return len(S) == 1

def inputnol(S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            return KonsLo(FirstList(S), inputnol(TailList(S)))
        elif FirstList(S) == []:
            return KonsLo([0], inputnol(TailList(S)))
        else:
            return KonsLo(inputnol(FirstList(S)), inputnol(TailList(S)))
        
def ToListBiasa(S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            return KonsLo(FirstList(S), ToListBiasa(TailList(S)))
        else:
            return ToListBiasa(FirstList(S)) + ToListBiasa(TailList(S))

def Rember_V1(X, L):
    if IsEmpty(L):
        return []
    else:
        if FirstList(L) == X:
            return TailList(L)
        else:
            return KonsLo(FirstList(L), Rember_V1(X, TailList(L)))
        
def MinELmt(H):
    if IsOneElmt(H):
        return FirstList(H)
    else:
        if FirstList(H) < LastList(H):
            return MinELmt(HeadList(H))
        else:
            return MinELmt(TailList(H))

def MinList(H):
    if IsEmpty(H):
        return []
    else:
        return KonsLo(MinELmt(H), MinList(Rember_V1(MinELmt(H), H)))

def remove(L1, L2):
    if IsEmpty(L1):
        return L2
    else:
        if IsAtom(FirstList(L2)):
            return remove(TailList(L1), TailList(L2))
        else:
            return KonsLo(remove(FirstList(L1), FirstList(L2)), remove(TailList(L1), TailList(L2)))
 
def Ubah(S1, S2):
    if IsEmpty(S2):
        return []
    else:
        if IsAtom(FirstList(S2)):
            return KonsLo(FirstList(S1), Ubah(TailList(S1), TailList(S2)))
        else:
            return KonsLo(Ubah(S1, FirstList(S2)), Ubah(remove(ToListBiasa(Ubah(S1, FirstList(S2))), ToListBiasa(S1)), TailList(S2)))
        
def ArusPenata(S):
    if IsEmpty(S):
        return [0]
    else:
        return Ubah(MinList(ToListBiasa(inputnol(S))), inputnol(S))

print(ArusPenata([1,[[],2,[3,[[],[4,[5,[],[[6]]]],7]],[8,[[],9,[10,[[[],11],12]]]],13],[[14,[[],15]],16,[17,[18,[[],[],[19]]]]],[20,[],[21,[22,[23,[],[[[24]]]]]],[[25,[[],26]]]],27,[28,[29,[[],30,[31,[],[[[32]]]]]]],[[33,[],[34,[[],35]]]],36,[37,[[],38,[39,[],[[40,[[],41]]]]]],42,[43,[[],44,[45,[],[[46,[[],47]]]]]],48,[49,[],[50,[[],51,[[[52]]]]]],53,[54,[55,[[],56],[[],57,[58,[[],59]]]]],[[60,[[],[],61]]],62,[63,[[],64,[65,[],[[66]]]]],[[[[67]]]],68,[69,[],[70,[71,[[],72,[[73]]]]]],74,[75,[[],76],[77,[],[[78,[[],79]]]]],80,[81,[82,[83,[],[[84,[[],85]]]]]],[[86,[[],87]]],[[88,[89,[[],90]]]],91,[92,[],93],[[94,[95,[[],[],96]]]],97,[98,[99,[],[[100,[[],101]]]]]]))
print(ArusPenata([[[[[[[[[[[],[[],[[[[],[]]],[]]]],[[],[[[[[]]]]]]]]],[[[],[],[[[[[]]]]]]]]]]]]]))
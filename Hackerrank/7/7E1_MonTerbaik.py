# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePokemon: string, 2 integer --> Pokemon
# MakePokemon(Nama, ATK, SP_ATK) mendefinisikan sebuah Pokemon dengan Nama dan stat ATK serta Special ATK-nya.
def MakePokemon(Nama, ATK, SP_ATK):
    return [Nama, ATK, SP_ATK]

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstElmt: List --> elmt
# FirstElmt(L) mengembalikan elemen pertama list L
def FirstPokemon(L):
    return L[0]

# LastElmt: List --> elmt
# LastElmt(L) mengembalikan elemen terakhir list L
def LastPokemon(L):
    return L[-1]

# Head: List --> List
# Head(L) mengembalikan list L tanpa elemen pertama, mungkin kosong
def Head(L):
    return L[:-1]

# Tail: List --> List
# Tail(L) mengembalikan list L tanpa elemen terakhir, mungkin kosong
def Tail(L):
    return L[1:]

# NamaPK: Pokemon --> string
# NamaPK(P) Mengembalikan nama dari Pokemon P
def NamaPK(P):
    return P[0]

# ATK: Pokemon --> integer
# ATK(P) Mengembalikan ATK dari Pokemon P
def ATK(P):
    return P[1]

# SP_ATK: Pokemon --> integer
# SP_ATK(P) Mengembalikan SP_ATK dari Pokemon P
def SP_ATK(P):
    return P[2]

def IsEmpty(P):
    return P == []

def TerbaikInPC(P):
    if IsEmpty(Tail(P)):
        return NamaPK(FirstPokemon(P))
    elif ATK(FirstPokemon(P)) >= ATK(LastPokemon(P)) and ATK(FirstPokemon(P)) > SP_ATK(LastPokemon(P)):
        return TerbaikInPC(Head(P))
    elif ATK(FirstPokemon(P)) == SP_ATK(LastPokemon(P)):
        if SP_ATK(FirstPokemon(P)) >= ATK(LastPokemon(P)):
            return TerbaikInPC(Head(P))
        else:
            return TerbaikInPC(Tail(P))
    else:
        return TerbaikInPC(Tail(P))
        
print(TerbaikInPC([MakePokemon('Sceptile', 308, 222), MakePokemon('Salamance', 229, 308), MakePokemon('Lucario', 3080, 222)]))
print(TerbaikInPC([MakePokemon('Scizor', 344, 151), MakePokemon('Electivire', 244, 344), MakePokemon('Urshifu', 344, 151), MakePokemon('Beedrill', 201, 88)]))
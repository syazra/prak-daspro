#Nama File: list.py
#Deskripsi: berisi type dan operasi list of list
#Pembuat: 
#Tanggal:

from ListOfList import *

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def makePN(A,PN):
    return [A,PN]

#DEFINISI DAN SPESIFIKASI SELEKTOR
def Akar(PN):
    return PN[0]

def Anak(PN):
    return PN[1]

#DEFINISI DAN SPESIFIKASI PREDIKAT
def isTreeNEmpty(PN):
    return PN == []

def isOneElmt(PN):
    return (isTreeNEmpty(PN) == False) and (isTreeNEmpty(Anak(PN)) == True)

def PrintTreeNAryHelp(T, sisa, indent):
    print(indent + str(Akar(T)))
    if not isEmpty(Anak(T)):
        PrintTreeNAryHelp(FirstList(Anak(T)), TailList(Anak(T)), indent + '\t')
    if not isEmpty(sisa):
        PrintTreeNAryHelp(FirstList(sisa), TailList(sisa), indent)

def PrintTreeNAry(T):
    PrintTreeNAryHelp(T, [], '')


def NbNElmt(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0
    
    # Jika hanya ada satu elemen (Akar saja)
    if isOneElmt(PN):
        return 1
    
    # Hitung 1 untuk Akar, dan rekursif pada setiap Anak pohon
    # Tanpa menggunakan loop, kita memanggil fungsi untuk setiap Anak secara rekursif
    # Pertama pada Anak pertama
    return 1 + NbNElmt(FirstList(Anak(PN))) + NbNElmtChild(TailList(Anak(PN)))

# Fungsi tambahan untuk menghitung jumlah elemen pada sisa Anak-Anak
def NbNElmtChild(PN):
    # Basis: Jika tidak ada Anak
    if isTreeNEmpty(PN):
        return 0
    
    # Jika ada Anak, rekursif pada Anak pertama dan sisa Anak-Anak
    return NbNElmt(FirstList(PN)) + NbNElmtChild(TailList(PN))

def NbNDaun(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0
    
    # Jika pohon adalah daun (Anak kosong)
    if isOneElmt(PN) and isTreeNEmpty(Anak(PN)):
        return 1
    
    # Rekursi pada Akar dan Anak-Anak
    return NbNDaunChild(Anak(PN))

# Fungsi tambahan untuk menghitung jumlah daun pada sisa Anak-Anak
def NbNDaunChild(PN):
    # Basis: Jika tidak ada Anak
    if isTreeNEmpty(PN):
        return 0
    
    # Jika ada Anak, rekursif pada Anak pertama dan sisa Anak-Anak
    return NbNDaun(FirstList(PN)) + NbNDaunChild(TailList(PN))

def NbNElmt(PN):
    # Basis: Jika pohon kosong
    if isTreeNEmpty(PN):
        return 0
    
    # Jika hanya ada satu elemen (Akar saja)
    if isOneElmt(PN):
        return 1
    
    # Hitung 1 untuk Akar, dan rekursif pada setiap Anak pohon
    # Tanpa menggunakan loop, kita memanggil fungsi untuk setiap Anak secara rekursif
    # Pertama pada Anak pertama
    return 1 + NbNElmt(FirstList(Anak(PN))) + NbNElmtChild(TailList(Anak(PN)))

# Fungsi tambahan untuk menghitung jumlah elemen pada sisa Anak-Anak
def NbNElmtChild(PN):
    # Basis: Jika tidak ada Anak
    if isTreeNEmpty(PN):
        return 0
    
    # Jika ada Anak, rekursif pada Anak pertama dan sisa Anak-Anak
    return NbNElmt(FirstList(PN)) + NbNElmtChild(TailList(PN))

def GetHelp(j, pohon):
    if isTreeNEmpty(pohon):
        return False
    else:
        if IsSearchXTree(j, FirstList(pohon)):
            return True
        else:
            return GetHelp(j, TailList(pohon))


def IsSearchXTree(X, T):
    if isTreeNEmpty(T):
        return False
    elif isOneElmt(T):
        return X==T
    elif FirstList(T) == X:
        return True
    else:
        if IsSearchXTree(X, FirstList(Anak(T))):
            return True
        else:
            return GetHelp(X, TailList(Anak(T)))
    

#APLIKASI
T = makePN(2,[])
PrintTreeNAry(makePN(2,[]))
print(isTreeNEmpty(T))
print(isOneElmt(T))
T2 = makePN('A',[])
PrintTreeNAry(T2)
print(NbNElmt(T2))
print(NbNDaun(T2))
print(IsSearchXTree("Raffi", makePN("Ridho",[makePN("Silvani", [makePN("Nuha",[]), makePN("Syahrafi",[makePN("Ega", [])]), 
                                                                makePN("Noci",[])]), makePN("Rendi",[makePN("Fikhrul",[])]), 
                                                                makePN("Ruth",[makePN("Aji",[])]), makePN("Eko",[makePN("Raffi",[])])])))
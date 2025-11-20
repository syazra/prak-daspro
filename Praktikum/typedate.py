# Nama file  : typedate.py
# Pembuat    : Syafira Azka Ramadhani
# Tanggal    : 29 September 2024
# Deskripsi  : Membuat type bentukan date beserta konstruktor, selektor, operator, dan predikatnya


# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type date: <Hr: integer[1,2,..,31], Bln: integer[1,2,..,12], Thn: integer>0>
# <Hr: integer[1,2,..,31], Bln: integer[1,2,..,12], Thn: integer>0> adalah tanggal Hr bulan Bln tahun Thn

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeDate: integer[1,2,..,31], integer[1,2,..,12], integer>0 --> date
# MakeDate(Hr,Bln,Thn) adalah tanggal pada hari, bulan, dan tahun yang bersangkutan
# REALISASI
def MakeDate(Hr,Bln,Thn):
    return [Hr,Bln,Thn]

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# Day: date --> Hr
# Day(D) memberikan hari Hr dari D yang terdiri dari [Hr,Bln,Thn]
# REALISASI
def Day(D):
    return D[0]

# Month: date --> Bln
# Month(D) memberikan bulan Bln dari D yang terdiri dari [Hr,Bln,Thn]
# REALISASI
def Month(D):
    return D[1]

# Year: date --> Thn
# Year(D) memberikan tahun Thn dari D yang terdiri dari [Hr,Bln,Thn]
# REALISASI
def Year(D):
    return D[2]

# ===========================================================================================================================

# DEFINSI DAN SPESIFIKASI OPERATOR
# NextDay: date --> date
# NextDay(D) menghitung date yang merupakan keesokan hari dari date D yang diberikan
# REALISASI
def NextDay(D):
    if Month(D) == 1 or Month(D) == 3 or Month(D) == 5 or Month(D) == 7 or Month(D) == 8 or Month(D) == 10 or Month(D) == 12:
        if Day(D) < 31:
            return MakeDate(Day(D) + 1, Month(D),Year(D))
        elif Day(D) == 31 and Month(D) == 12:
            return MakeDate(1,1,Year(D) + 1)
        else:
            return MakeDate(1,Month(D) + 1,Year(D))
    elif Month(D) == 2:
        if Day(D) < 28:
            return MakeDate(Day(D) + 1,Month(D),Year(D))
        else:
            if Day(D) == 28 and IsKabisat(D):
                return MakeDate(29,2,Year(D))
            else:
                return MakeDate(1,Month(D) + 1,Year(D))
    elif Month(D) == 4 or Month(D) == 6 or Month(D) == 9 or Month(D) == 11:
        if Day(D) < 30:
            return MakeDate(Day(D) + 1,Month(D),Year(D))
        else:
            return MakeDate(1,Month(D),Year(D))

# Yesterday: date --> date
# Yesterday(D) menghitung date yang merupakan 1 hari sebelum date D yang diberikan
# REALISASI
def Yesterday(D):
    if Day(D) == 1:
        if Month(D) == 5 or Month(D) == 7 or Month(D) == 10 or Month(D) == 12:
            return MakeDate(30,Month(D) - 1,Year(D))
        elif Month(D) == 3:
            if IsKabisat(D):
                return MakeDate(29,2,Year(D))
            else:
                return MakeDate(28,2,Year(D))
        elif Month(D) == 2 or Month(D) == 4 or Month(D) == 6 or Month(D) == 8 or Month(D) == 9 or Month(D) == 11:
            return MakeDate(31,Month(D) - 1,Year(D))
        elif Month(D) == 1:
            return MakeDate(31,12,Year(D) - 1)
    else:
        return MakeDate(Day(D)-1,Month(D),Year(D))

# dpm: date --> integer[1,32,..,355]
# dpm(D) adalah jumlah hari pada tanggal 1 dari bulan Bln dari date D yang terhitung mulai 1 Januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan Bln dari date D, tanpa memperhitungkan tahun kabisat
# REALISASI
def dpm(D):
    if Month(D)==1:
        return 1
    elif Month(D)==2:
        return 32
    elif Month(D)==3:
        return 60
    elif Month(D)==4:
        return 91
    elif Month(D)==5:
        return 121
    elif Month(D)==6:
        return 152
    elif Month(D)==7:
        return 182
    elif Month(D)==8:
        return 213
    elif Month(D)==9:
        return 244
    elif Month(D)==10:
        return 274
    elif Month(D)==11:
        return 305
    elif Month(D)==12:
        return 335
    
# HariKe1900: date --> integer[1,2,..,366]
# HariKe1900(D) menghitung jumlah hari terhadap 1 Januari pada tahun Thn dari date D, dengan memperhitungkan apakah tahun Thn dari date D adalah tahun kabisat
# REALISASI    
def HariKe1900(D):
    if Month(D) > 2 and IsKabisat(D):
        return dpm(D) + Day(D)
    else:
        return dpm(D) + Day(D) - 1

# ===========================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqD: 2 date --> boolean
# IsEqD(D1,D2) true jika D1=D2 dengan mengirimkan Hr1=Hr2 dan Bln1=Bln2 dan Thn1=Thn2
# REALISASI
def IsEqD(D1,D2):
    return Day(D1) == Day(D2) and Month(D1) == Month(D2) and Year(D1) == Year(D2)

# IsBefore: 2 date --> boolean
# IsBefore(D1,D2) true jika D1 adalah sebelum D2 dengan mengirimkan Thn1<Thn2 atau Bln1<Bln2 atau Hr1<Hr2
# REALISASI
def IsBefore(D1,D2):
    if Year(D1) != Year(D2):
        return Year(D1) < Year(D2)
    else:
        if Month(D1) != Month(D2):
            return Month(D1) < Month(D2)
        else:
            if Day(D1) != Day(D2):
                return Day(D1) < Day(D2)
            else:
                return False

# IsAfter: 2 date --> boolean
# IsAfter(D1,D2) true jika D1 adalah sesudah D2 dengan mengirimkan Thn1>Thn2 atau Bln1>Bln2 atau Hr1>Hr2
# REALISASI
def IsAfter(D1,D2):
    if Year(D1) != Year(D2):
        return Year(D1) > Year(D2)
    else:
        if Month(D1) != Month(D2):
            return Month(D1) > Month(D2)
        else:
            if Day(D1) != Day(D2):
                return Day(D1) > Day(D2)
            else:
                return False

# IsKabisat: date --> boolean
# IsKabisat(D) true jika Thn dari date D habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400
# REALISASI
def IsKabisat(D):
    return ((Year(D) % 4 == 0) and (Year(D) % 100 != 0)) or (Year(D) % 400 == 0)

# ===========================================================================================================================

# APLIKASI
print(NextDay(MakeDate(28,2,2008)))
print(Yesterday(MakeDate(1,1,2024)))
print(HariKe1900(MakeDate(29,2,2000)))
print(IsEqD(MakeDate(15,10,2006),MakeDate(15,10,2006)))
print(IsBefore(MakeDate(10,1,1999),MakeDate(9,1,2000)))
print(IsAfter(MakeDate(14,10,2001),MakeDate(15,10,2003)))
print(IsKabisat(MakeDate(14,10,1000)))
# Nama file  : typemahasiswa.py
# Pembuat    : Syafira Azka Ramadhani
# Tanggal    : 30 September 2024
# Deskripsi  : Membuat tipe bentukan MHS1, MHS2, dan MHS3 beserta konstruktor, selektor, dan operatornya


#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type MHS1: <NIM: string, Nama: string, TanggalLahir: string>
# <NIM: string, Nama: string, TanggalLahir: string> adalah tipe bentukan yang berisi informasi dasar, yaitu NIM, Nama, dan Tanggal Lahir mahasiswa

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MHS1: 3 string --> MHS1 
# MHS1(NIM,Nama,TanggalLahir) adalah tipe bentukan yang berisi informasi dasar, yaitu NIM, Nama, dan Tanggal Lahir mahasiswa
# REALISASI
def MHS1(NIM,Nama,TanggalLahir):
    return [NIM,Nama,TanggalLahir]

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# NIM1: MHS1 --> string
# NIM1(M1) memberikan NIM mahasiswa dari data MHS1
# REALISASI
def NIM1(M1):
    return M1[0]

# Nama: MHS1 --> string
# Nama(M1) memberikan Nama mahasiswa dari data MHS1
# REALISASI    
def Nama(M1):
    return M1[1]

# TanggalLahir: MHS1 --> string
# TanggalLahir(M1) memberikan TanggalLahir mahasiswa dari data MHS1
# REALISASI
def TanggalLahir(M1):
    return M1[2]

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type MHS2: <NIM: string, KodeMatkul: string, Nilai: real>
# <NIM: string, KodeMatkul: string, Nilai: real> adalah tipe bentukan yang berisi informasi nilai, yaitu NIM, KodeMatkul, dan Nilai

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MHS2: 2 string, real --> MHS2
# MHS2(NIM,KodeMatkul,Nilai) adalah tipe bentukan yang berisi informasi nilai, yaitu NIM, KodeMatkul, dan Nilai mahasiswa
# REALISASI
def MHS2(NIM,KodeMatkul,Nilai):
    return [NIM,KodeMatkul,Nilai]

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# NIM2: MHS2 --> string
# NIM2(M2) memberikan NIM mahasiswa dari data MHS2
# REALISASI
def NIM2(M2):
    return M2[0]

# KodeMatkul1: MHS2 --> string
# KodeMatkul1(M2) memberikan KodeMatkul dari data MHS2
# REALISASI
def KodeMatkul1(M2):
    return M2[1]

# Nilai: MHS2 --> real
# Nilai(M2) memberikan Nilai mahasiswa dari data MHS2
# REALISASI
def Nilai(M2):
    return M2[2]

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# type MHS3: <KodeMatkul: string, NamaMatkul: string>
# <KodeMatkul: string, NamaMatkul: string> adalah tipe bentukan yang berisi informasi matkul, yaitu KodeMatkul dan NamaMatkul

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MHS3: 2 string --> MHS3
# MHS3(KodeMatkul,NamaMatkul) adalah tipe bentukan yang berisi informasi matkul, yaitu KodeMatkul dan NamaMatkul
# REALISASI
def MHS3(KodeMatkul,NamaMatkul):
    return [KodeMatkul,NamaMatkul]

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# KodeMatkul2: MHS3 --> string
# KodeMatkul2(M3) memberikan KodeMatkul dari data MHS3
# REALISASI
def KodeMatkul2(M3):
    return M3[0]

# NamaMatkul: MHS3 --> string
# NamaMatkul(M3) memberikan NamaMatkul dari data MHS3
# REALISASI
def NamaMatkul(M3):
    return M3[1]

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI TYPE
# NilaiMHS: <KodeMatkul: string, NilaiTertinggi: real, NilaTerendah: real, RangeNilai: real>
# <KodeMatkul: string, NilaiTertinggi: real, NilaTerendah: real, RangeNilai: real> adalah tipe bentukan yang berisi informasi nilai, yaitu KodeMatkul, NilaiTertinggi, NilaiTerendah, dan RangeNilai

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# NilaiMHS: string, 3 real --> NilaiMHS
# NilaiMHS(KodeMatkul,NilaiTertinggi,NilaiTerendah,RangeNilai) tipe bentukan yang berisi informasi nilai, yaitu KodeMatkul, NilaiTertinggi, NilaiTerendah, dan RangeNilai
# REALISASI
def NilaiMHS(KodeMatkul,NilaiTertinggi,NilaiTerendah,RangeNilai):
    return [KodeMatkul,NilaiTertinggi,NilaiTerendah,RangeNilai]

#==============================================================================================================================

# DEFINISI DAN SPESIFIKASI OPERATOR
# hitungRangeNilai: 3 MHS2 --> NilaiMHS
# hitungRangeNilai(M1,M2,M3) adalah fungsi untuk menghitung range (selisih nilai tertinggi dan terendah) dari nilai mahasiswa dan mengembalikan sebuah tipe bentukan NilaiMHS yang memuat: KodeMatkul, NilaiTertinggi, NilaiTerendah, RangeNilai tetapi jika KodeMatkul tidak ada yang sama akan mengembalikan <0,0,0,0>
# REALISASI
def hitungRangeNilai(M1,M2,M3):
    if KodeMatkul1(M1) == KodeMatkul1(M2) and KodeMatkul1(M2) == KodeMatkul1(M3):
        return NilaiMHS(KodeMatkul1(M1) , max(max(Nilai(M1),Nilai(M2)),Nilai(M3)) , min(min(Nilai(M1),Nilai(M2)),Nilai(M3)) ,
                max(max(Nilai(M1),Nilai(M2)),Nilai(M3)) - min(min(Nilai(M1),Nilai(M2)),Nilai(M3)))
    elif KodeMatkul1(M1) == KodeMatkul1(M2) and KodeMatkul1(M1) != KodeMatkul1(M3):
        return NilaiMHS(KodeMatkul1(M1) , max(Nilai(M1),Nilai(M2)) , min(Nilai(M1),Nilai(M2)) , max(Nilai(M1),Nilai(M2)) - min(Nilai(M1),Nilai(M2)))
    elif KodeMatkul1(M2) == KodeMatkul1(M3) and KodeMatkul1(M2) != KodeMatkul1(M1):
        return NilaiMHS(KodeMatkul1(M2) , max(Nilai(M2),Nilai(M3)) , min(Nilai(M2),Nilai(M3)) , max(Nilai(M2),Nilai(M3)) - min(Nilai(M2),Nilai(M3)))
    elif KodeMatkul1(M1) == KodeMatkul1(M3) and KodeMatkul1(M2) != KodeMatkul1(M3):
        return NilaiMHS(KodeMatkul1(M1) , max(Nilai(M1),Nilai(M3)) , min(Nilai(M1),Nilai(M3)) , max(Nilai(M1),Nilai(M3)) - min(Nilai(M1),Nilai(M3)))
    else:
        return NilaiMHS(0,0,0,0)

# max: 2 real --> real
# max(x,y) mengembalikan nilai maksimum dari dua buah bilangan real
# REALISASI
def max(x,y):
    return (x+y+abs(x-y))/2

# min: 2 real --> real
# min(x,y) mengembalikan nilai minimum dari dua buah bilangan real
# REALISASI
def min(x,y):
    return (x+y-abs(x-y))/2

#==============================================================================================================================

# APLIKASI
print(hitungRangeNilai(MHS2("24060123120024","IF101",85.0),MHS2("24060123120024","IF101",90.0),MHS2("24060123120024","IF101",75.0)))
print(hitungRangeNilai(MHS2("24060123120024","IF102",85.0),MHS2("24060123120024","IF102",90.0),MHS2("24060123120024","IF101",75.0)))
print(hitungRangeNilai(MHS2("24060123120024","IF101",85.0),MHS2("24060123120024","IF102",90.0),MHS2("24060123120024","IF101",75.0)))
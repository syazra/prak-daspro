def makeMHS(NIM, Nama, TanggalLahir, MataKuliah):
    return [NIM, Nama, TanggalLahir, MataKuliah]

def NIM(M):
    return M[0]
  
def Nama(M):
    return M[1]

def TanggalLahir(M):
    return M[2]

def MK(M):
    return M[3]

def makeMK(NIM, KodeMatkul, Nilai):
    return [NIM, KodeMatkul, Nilai]

def NIM(MK):
    return MK[0]

def KodeMatkul(MK):
    return MK[1]

def Nilai(MK):
    return MK[2]

def max2(a, b):
    return a if (a > b) else b

def min2(a, b):
    return a if (a < b) else b

def rangeNilai(M1, M2, M3, M4, M5):
    return (max2(max2(max2(Nilai(MK(M1)), Nilai(MK(M2))), max2(Nilai(MK(M3)), Nilai(MK(M4)))), Nilai(MK(M5))) -
            min2(min2(min2(Nilai(MK(M1)), Nilai(MK(M2))), min2(Nilai(MK(M3)), Nilai(MK(M4)))), Nilai(MK(M5))))
    
def isLulusMK(M):
    return Nilai(MK(M)) > 75

print(rangeNilai(makeMHS('101', 'A', '01/01/01', makeMK('101', 'A', 90)),
                 makeMHS('101', 'A', '01/01/01', makeMK('101', 'A', 91)),
                 makeMHS('101', 'A', '01/01/01', makeMK('101', 'A', 99)),
                 makeMHS('101', 'A', '01/01/01', makeMK('101', 'A', 95)),
                 makeMHS('101', 'A', '01/01/01', makeMK('101', 'A', 100))))

print(isLulusMK(makeMHS('101', 'A', '01/01/01', makeMK('101', 'A', 85))))
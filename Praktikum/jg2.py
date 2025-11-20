def MHS1(NIM,Nama,TanggalLahir):
    return [NIM,Nama,TanggalLahir]

def NIM1(M1):
    return M1[0]
    
def Nama(M1):
    return M1[1]

def TanggalLahir(M1):
    return M1[2]

#######################################

def MHS2(NIM,KodeMatkul,Nilai):
    return [NIM,KodeMatkul,Nilai]

def NIM2(M2):
    return M2[0]

def KodeMatkul1(M2):
    return M2[1]

def Nilai(M2):
    return M2[2]

#######################################

def MHS3(KodeMatkul,NamaMatkul):
    return [KodeMatkul,NamaMatkul]

def KodeMatkul2(M3):
    return M3[0]

def NamaMatkul(M3):
    return M3[1]

#######################################

def hitungRangeNilai(M1,M2,M3):
    if NIM2(M1) == NIM2(M2) and NIM2(M1 )== NIM2(M3):
        if KodeMatkul1(M1) == KodeMatkul1(M2) and KodeMatkul1(M1) == KodeMatkul1(M3):
            return (KodeMatkul1(M1) , max(max(Nilai(M1),Nilai(M2)),Nilai(M3)) , min(min(Nilai(M1),Nilai(M2)),Nilai(M3)) ,
                max(max(Nilai(M1),Nilai(M2)),Nilai(M3)) - min(min(Nilai(M1),Nilai(M2)),Nilai(M3)))
        elif KodeMatkul1(M1) == KodeMatkul1(M2) and KodeMatkul1(M1) != KodeMatkul1(M3):
            if Nilai(M1) >= Nilai(M2):
                return KodeMatkul1(M1) , Nilai(M1) , min(Nilai(M1),Nilai(M2)) , Nilai(M1) - min(Nilai(M1),Nilai(M2))
            else:
                return KodeMatkul1(M2) , Nilai(M2) , min(Nilai(M1),Nilai(M2)) , Nilai(M2) - min(Nilai(M1),Nilai(M2))
        elif KodeMatkul1(M2) == KodeMatkul1(M3) and KodeMatkul1(M2) != KodeMatkul1(M1):
            if Nilai(M2) >= Nilai(M3):
                return KodeMatkul1(M2) , Nilai(M2) , min(Nilai(M2),Nilai(M3)) , Nilai(M2) - min(Nilai(M2),Nilai(M3))
            else:
                return KodeMatkul1(M3) , Nilai(M3) , min(Nilai(M2),Nilai(M3)) , Nilai(M3) - min(Nilai(M2),Nilai(M3))
        elif KodeMatkul1(M1) == KodeMatkul1(M3) and KodeMatkul1(M2) != KodeMatkul1(M3):
            if Nilai(M1) >= Nilai(M3):
                return KodeMatkul1(M1) , Nilai(M1) , min(Nilai(M1),Nilai(M3)) , Nilai(M1) - min(Nilai(M1),Nilai(M3))
            else:
                return KodeMatkul1(M3) , Nilai(M3) , min(Nilai(M1),Nilai(M3)) , Nilai(M3) - min(Nilai(M1),Nilai(M3))
        else:
            if Nilai(M1) >= Nilai(M2) and Nilai(M1) >= Nilai(M3):
                return KodeMatkul1(M1) , Nilai(M1) , Nilai(M1) , 0.0
            elif Nilai(M2) >= Nilai(M1) and Nilai(M2) >= Nilai(M3):
                return KodeMatkul1(M2) , Nilai(M2) , Nilai(M2) , 0.0
            else:
                return KodeMatkul1(M3) , Nilai(M3) , Nilai(M3) , 0.0     
    elif NIM2(M1) == NIM2(M2) and NIM2(M1) != NIM2(M3):
        if Nilai(M1) >= Nilai(M2):
            return KodeMatkul1(M1) , Nilai(M1) , min(Nilai(M1),Nilai(M2)) , Nilai(M1) - min(Nilai(M1),Nilai(M2))
        else:
            return KodeMatkul1(M2) , Nilai(M2) , min(Nilai(M1),Nilai(M2)) , Nilai(M2) - min(Nilai(M1),Nilai(M2))
    elif NIM2(M2) == NIM2(M3) and NIM2(M2) != NIM2(M1):
        if Nilai(M2) >= Nilai(M3):
            return KodeMatkul1(M2) , Nilai(M2) , min(Nilai(M2),Nilai(M3)) , Nilai(M2) - min(Nilai(M2),Nilai(M3))
        else:
            return KodeMatkul1(M3) , Nilai(M3) , min(Nilai(M2),Nilai(M3)) , Nilai(M3) - min(Nilai(M2),Nilai(M3))
    elif NIM2(M1) == NIM2(M3) and NIM2(M2) != NIM2(M3):
        if Nilai(M1) >= Nilai(M3):
            return KodeMatkul1(M1) , Nilai(M1) , min(Nilai(M1),Nilai(M3)) , Nilai(M1) - min(Nilai(M1),Nilai(M3))
        else:
            return KodeMatkul1(M3) , Nilai(M3) , min(Nilai(M1),Nilai(M3)) , Nilai(M3) - min(Nilai(M1),Nilai(M3))
    else:
        if Nilai(M1) >= Nilai(M2) and Nilai(M1) >= Nilai(M3):
            return KodeMatkul1(M1) , Nilai(M1) , Nilai(M1) , 0.0
        elif Nilai(M2) >= Nilai(M1) and Nilai(M2) >= Nilai(M3):
            return KodeMatkul1(M2) , Nilai(M2) , Nilai(M2) , 0.0
        else:
            return KodeMatkul1(M3) , Nilai(M3) , Nilai(M3) , 0.0
    
print(hitungRangeNilai(MHS2("24060123120024","IF101",85.0),MHS2("24060123120024","IF102",90.0),MHS2("24060123120024","IF100",75.0)))
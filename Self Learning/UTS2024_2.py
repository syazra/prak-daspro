def MakeMahasiswa(NIM,Nama,Tugas,UTS,UAS):
    return [NIM,Nama,Tugas,UTS,UAS]

def NIM(mhs):
    return mhs[0]

def Nama(mhs):
    return mhs[1]

def Tugas(mhs):
    return mhs[2]

def UTS(mhs):
    return mhs[3]

def UAS(mhs):
    return mhs[4]
    
def NilaiMHS(Nama,NilaiHuruf):
    return [Nama,NilaiHuruf]

def HitungNilaiAkhir(mhs):
    return (40/100) * Tugas(mhs) + (30/100) * UTS(mhs) + (30/100) * UAS(mhs)

def Nilai(mhs):
    if 80.0 <= HitungNilaiAkhir(mhs) <= 100.0:
        return NilaiMHS(Nama(mhs), 'A')
    elif 60.0 <= HitungNilaiAkhir(mhs) < 80.0:
        return NilaiMHS(Nama(mhs), 'B')
    elif 40.0 <= HitungNilaiAkhir(mhs) < 60.0:
        return NilaiMHS(Nama(mhs), 'C')
    elif 20.0 <= HitungNilaiAkhir(mhs) < 40.0:
        return NilaiMHS(Nama(mhs), 'D')
    elif 0.0 <= HitungNilaiAkhir(mhs) < 20.0:
        return NilaiMHS(Nama(mhs), 'E')
    
print(Nilai(MakeMahasiswa("2", "Lala", 90.0, 30.0, 20.0)))
# Nama file: EstimateGreatLib.py
# Pembuat: Syafira Azka Ramadhani
# Tanggal: 20 September 2024
# Deskripsi: EstimateGreatLib(D,X,Y,SS,SR,AS,AM,AIP,R)

# Definisi dan spesifikasi dari fungsi EstimateGreatLib(D,X,Y,SS,SR,AS,AM,AIP,R)
# EstimateGreatLib : string, 4 integer[0,1,2,...,24], 3 integer[0,1,2,...,10000], integer[1,2,3,...,100] --> real
# EstimateGreatLib(D,XY,SS,SR,AS,AM,AIP,R) menghitung estimasi perbandingan banyaknnya pengunjung di hari D mulai dari pukul X hingga pukul Y dengan bantuan perkiraan dari Ahli Statistika (AS), Ahli Matematika (AM), dan Ahli Ilmu Perpustakaan (AIP); serta persentase R.
# pers1 : string, 4 integer[0,1,2,...24], 3 integer[0,1,2,...,10000], integer[1,2,3,...,100]
# pers1(D,X,Y,SS,SR,AS,AM,AIP,R) menghitung estimasi perbandingan banyaknnya pengunjung di hari D mulai dari pukul X hingga pukul Y dengan bantuan perkiraan dari Ahli Statistika (AS), Ahli Matematika (AM), dan Ahli Ilmu Perpustakaan (AIP); serta persentase R.
# rerata : string --> real
# rerata(D) menghitung rata-rata banyaknya pengunjung pada tiga pekan sebelumnya.
# ahli : 3 integer[0,1,2,...,10000] --> integer
# ahli(AS,AM,AIP) menghitung jangkauan atau range dari perkiraan ketiga ilmuwan.
# min2 : 2 integer[0,1,2,...,10000] --> integer
# min2(x,y) mencari nilai minimum dari dua ilmuwan.
# max2 : 2 integer[0,1,2,...,10000] --> integer 
# max2 (x,y) mencari nilai maximum dari dua ilmuwan.

# Realisasi
def max2(x,y):
    return (x + y + abs(x - y)) / 2

def min2(x,y):
    return (x + y - abs(x - y)) / 2

def ahli(AS,AM,AIP):
    return max2(max2(AS,AM),AIP) - min2(min2(AS,AM),AIP)

def rerata(D):
    if D == "senin":
        return (5000+6000+4000) / 3
    elif D == "selasa":
        return (7000+5000+2000) / 3
    elif D == "rabu":
        return (4500+3500+3000) / 3
    elif D == "kamis":
        return (2900+2100+2000) / 3
    elif D == "jumat":
        return (3000+3000+3000) / 3
    elif D == "sabtu":
        return (2000+2500+2300) / 3
    elif D == "minggu":
        return (1100+900+1000) / 3

def pers1(D,X,Y,SS,SR,AS,AM,AIP,R):
    if (X>=SR and Y<=SS):
        return round(((Y-X)*(ahli(AS,AM,AIP)))/(rerata(D)),5)
    elif (X<SR and Y<=SR) or (X>=SS and Y>SS):
        return round(((Y-X)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100,5)
    elif (X<SR and Y<=SS):
        return round(((((SR-X)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100)+((Y-SR)*(ahli(AS,AM,AIP))/(rerata(D))))/2,5)
    elif (Y>SS and X>=SR):
        return round(((((Y-SS)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100)+((SS-X)*(ahli(AS,AM,AIP))/(rerata(D))))/2,5)
    elif (X<SR and Y>SS):
        return round(((((SR-X)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100)+((SS-SR)*(ahli(AS,AM,AIP))/(rerata(D)))+((((Y-SS)*(ahli(AS,AM,AIP)))/(rerata(D)))*R/100))/3,5)

def EstimateGreatLib(D,X,Y,SS,SR,AS,AM,AIP,R):
    return pers1(D,X,Y,SS,SR,AS,AM,AIP,R)

print(EstimateGreatLib("jumat", 7, 8, 17, 6, 4000, 5500, 5000, 3))
print(EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50))
print(EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75))
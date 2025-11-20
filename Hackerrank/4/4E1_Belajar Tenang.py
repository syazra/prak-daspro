# Nama file: BelajarTenang.py
# Pembuat: Syafira Azka Ramadhani
# Tanggal: 17 September 2024
# Deskripsi: BelajarTenang(dB,m) menghitung berapa jarak minimal yang harus mereka tempuh agar suara sound system yang mereka dengar tidak melebihi 40 dB dan mengetahui apakah bensinnya cukup untuk menempuh atau tidak, apabila diketahui motornya hanya dapat menempuh m meter saja dengan bensin yang ada.

# Definisi dan spesifikasi dari fungsi BelajarTenang(dB,m):
# BelajarTenang : 2 integer[1,2,3,...,1000000] --> real
# BelajarTenang(dB,m) menghitung berapa jarak minimal yang harus mereka tempuh agar suara sound system yang mereka dengar tidak melebihi 40 dB dan mengetahui apakah bensinnya cukup untuk menempuh atau tidak, apabila diketahui motornya hanya dapat menempuh m meter saja dengan bensin yang ada.
# x2 : 2 integer[1,2,3,...,1000000], real --> real
# x2(dB,m,x1) adalah fungsi untuk mengetahui apakah bensinnya cukup untuk menempuh atau tidak, apabila diketahui motornya hanya dapat menempuh m meter saja dengan bensin yang ada.
# x1 : integer[1,2,3,...,1000000] --> real
# x1(dB) menghitung berapa jarak minimal yang harus mereka tempuh agar suara sound system yang mereka dengan tidak melebihi 40 dB.

# Realisasi
def x1(dB):
    return (15 * 10 ** ((dB - 40) / 20))

a=" meter"
def x2(dB,m,x1):
    if 15 * 10 ** ((dB - 40) / 20) > m:
        return "Isi bensin dulu, bang"
    else:
        return str(round(x1, 3)) + str(a)

def BelajarTenang(dB,m):
    return x2(dB,m,x1(dB))

# Aplikasi
print(BelajarTenang(102, 20000))
print(BelajarTenang(100, 1300))
# Nama file: jam.py
# Pembuat: Syafira Azka Ramadhani
# Tanggal: 17 September 2024
# Deskripsi: jam(j,m,s) menentukan apakah tiga bilangan integer j, m, dan s merupakan waktu yang valid, dan jika valid, cetak waktu tersebut dalam format: "Jam: j, Menit: m, Detik: s". Jika input tidak valid, program harus mencetak: "Waktu tidak valid"

# Definisi dan spesifikasi dari fungsi jam(j,m,s) adalah:
# jam : integer[0,1,2,...,24], integer[0,1,2,...,59], integer[0,1,2,...,59] --> string
# jam(j,m,s) menentukan apakah tiga bilangan integer j, m, dan s merupakan waktu yang valid, dan jika valid, cetak waktu tersebut dalam format: "Jam: j, Menit: m, Detik: s". Jika input tidak valid, program harus mencetak: "Waktu tidak valid"

# Realisasi
a="Jam: "
b=" Menit: "
c=" Detik: "
def jam(j,m,s):
    if 0 <= j and j <= 24 and 0 <= m and m <= 59 and 0 <= s and s <= 59:
        return str(a + str(j)) + "," + str(b + str(m)) + "," + str(c + str(s))
    else:
        return "Waktu tidak valid"
    
# Aplikasi
print(jam(12,30,45))
print(jam(12,45,60))
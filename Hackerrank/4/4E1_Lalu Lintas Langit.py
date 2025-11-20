# Nama file: monitor_pesawat.py
# Pembuat: Syafira Azka Ramadhani
# Tanggal: 17 September 2024
# Deskripsi: monitor_pesawat(x,y,z) memantau kondisi setiap pesawat dan memberikan status berdasarkan tiga parameter utama

# Definisi dan Spesifikasi dari fungsi monitor_pesawat(x,y,z) adalah:
# monitor_pesawat : 3 integer > 0 --> string
# monitor_pesawat memantau kondisi setiap pesawat dan memberikan status berdasarkan tiga parameter utama

# Realisasi
def monitor_pesawat(x,y,z):
    if y > 900 or y < 200:
        return "Kecepatan Berbahaya"
    elif x > 12000:
        return "Terlalu Tinggi"
    elif z < 20:
        return "Bahan Bakar Rendah"
    elif x < 5000 and 200 <= y and y <= 900 and z > 50:
        return "Aman untuk Mendarat"
    else:
        return "Berjalan Normal"

# Aplikasi
print(monitor_pesawat(4000,850,55))
print(monitor_pesawat(5000,950,70))
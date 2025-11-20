# Nama file: gradien.py
# Pembuat: Syafira Azka Ramadhani
# Tanggal: 17 September 2024
# Deskripsi: gradien(a,b) menghitung energi di titik-titik a dan b beserta gradien magisnya.

# Definisi dan spesifikasi dari fungsi gradien(a,b):
# gradien : 2 integer --> real
# gradien(a,b)
# f : integer --> 

def f(x):
    return 3 * x ** 2 + 2 * x - 5

def gradien(a,b):
    return (f(a) - f(b)) / (a-b)

print(f(5))
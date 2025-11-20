# Nama file: jalanSemut.py
# Pembuat: Syafira Azka Ramadhani
# Tanggal: 17 September 2024
# Deskripsi: jalanSemut(x,y,z) adalah fungsi untuk menemukan jalan mana yang semut pilih agar semut tersebut sampai ke gula melalui jalan tercepat dengan memasukkan input 3 buah bilangan integer > 0

# Definisi dan spesifikasi dari fungsi jalanSemut(x,y,z) adalah:
# jalanSemut : 3 integer > 0 --> real
# jalanSemut(x,y,z) adalah fungsi untuk menemukan jalan mana yang semut pilih agar semut tersebut sampai ke gula melalui jalan tercepat dengan memasukkan input 3 buah bilangan integer > 0
# js : 3 real > 0 --> real
# js(s1,s2,s3) adalah fungsi untuk membandingkan jalan mana yang semut pilih agar semut tersebut sampai ke gula melalui jalan tercepat
# s3 : 3 integer > 0 --> real
# s3(x,y,z) adalah fungsi untuk menghitung jalan semut dengan rumus: ((z + x)**2 + y**2)**0.5
# s2 : 3 integer > 0 --> real
# s2(x,y,z) adalah fungsi untuk menghitung jalan semut dengan rumus: ((y + z)**2 + x**2)**0.5
# s1 : 3 integer > 0 --> real
# s1(x,y,z) adalah fungsi untuk menghitung jalan semut dengan rumus: ((x + y)**2 + z**2)**0.5

#Realisasi
def s1(x,y,z):
    return round(((x + y)**2 + z**2)**0.5, 3)
def s2(x,y,z):
    return round(((y + z)**2 + x**2)**0.5, 3)
def s3(x,y,z):
    return round(((z + x)**2 + y**2)**0.5, 3)
def js(s1,s2,s3):
    if s1 < s2 and s1 < s3:
        return s1
    elif s2 < s1 and s2 < s3:
        return s2
    elif s3 < s1 and s3 < s1:
        return s3
def jalanSemut(x,y,z):
    return js(s1(x,y,z),s2(x,y,z),s3(x,y,z))

# Aplikasi
print(jalanSemut(3,4,5))
print(jalanSemut(1,2,7))
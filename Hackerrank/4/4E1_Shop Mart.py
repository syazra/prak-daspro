# Nama file: hargaAkhir.py
# Pembuat: Syafira Azka Ramadhani
# Tanggal: 20 September 2024
# Deskripsi: hargaAkhir(harga,kategori,VIP,lokasi,hari) adalah fungsi untuk menghitung harga akhir barang yang akan dibayar oleh pelanggan.

# Definisi dan spesifikasi dari fungsi hargaAkhir(harga,kategori,VIP,lokasi,hari):
# hargaAkhir : integer>0, string, boolean, 2 string --> integer
# hargaAkhir(harga,kategori,VIP,lokasi,hari) adalah fungsi untuk menghitung harga akhir barang yang akan dibayar oleh pelanggan.
# harga3 :integer>0, string --> real
# harga3(harga2,d) menghitung harga setelah diskon kategori produk dan hari pembelian dan ditambah dengan pajak lokasi pembelian.
# harga2 : integer>0, string, boolean, string --> real
# harga2(harga1,b,c,e) menghitung harga setelah diskon kategori produk dan menambah pajak atau mengurangi dengan diskon berdasarkan hari pembelian sesuai status keanggotaan.
# harga1 : integer>0, string, boolean --> real
# harga1(a,b,c) menghitung harga awal dikurangi dengan diskon kategori produk sesuai status keanggotaan.

# Realisasi
def harga1(a,b,c):
    if (b=="elektronik" and c==True):
        return a-(a*30/100)
    elif (b=="elektronik" and c==False):
        return a-(a*10/100)
    elif (b=="pakaian" and c==True):
        return a-(a*20/100)
    elif (b=="pakaian" and c==False):
        return a-(a*5/100)
    elif (b=="makanan" and c==True):
        return a-(a*15/100)
    elif (b=="makanan" and c==False):
        return a-(a*2/100)
    elif (b=="lainnya"):
        return a
def harga2(harga1,b,c,e):
    if (e=="Jumat" and c==True) or (e=="Sabtu" and c==True):
        return harga1-(harga1*5/100)
    elif (e=="Minggu"):
        return harga1+(harga1*5/100)
    elif (e=="Rabu" and b=="pakaian"):
        return harga1-(harga1*5/100)
    else:
        return harga1 
def harga3(harga2,d):
    if (d=="dalam negeri"):
        return harga2+(harga2*10/100)
    else:
        return harga2+(harga2*20/100)
def hargaAkhir(harga,kategori,VIP,lokasi,hari):
    return int(harga3(harga2(harga1(harga,kategori,VIP),kategori,VIP,hari),lokasi))

# Aplikasi
print(hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin"))
print(hargaAkhir(500000, "pakaian", False, "luar negeri", "Rabu"))
# Nama file: denumeratorSeq.py
# Pembuat: Syafira Azka Ramadhani
# Tanggal: 22 september 2024
# Deskripsi: denumeratorSeq(x) menentukan apakah urutan angka x terulang tersebut sesuai dengan desimal hasil pembagian 1 dengan sebuah bilangan bulat. Jika iya, berapa nilai bilangan bulat pembagi tersebut? Jika tidak, keluarkan string “Tidak ada”.

# Definisi dan spesifikasi dari fungsi denumeratorseq(x):
# denumeratorSeq : character --> string
# denumeratorSeq(x) menentukan apakah urutan angka x terulang tersebut sesuai dengan desimal hasil pembagian 1 dengan sebuah bilangan bulat. Jika iya, berapa nilai bilangan bulat pembagi tersebut? Jika tidak, keluarkan string “Tidak ada”.
# penyebut : character --> string
# penyebut(x) mengeluarkan penyebut 9 dikali dengan panjang string x.

# Realisasi
# a=9
# def penyebut(x):
#     return str(a)*len(str(x))

# b="Ada: "
# def denumeratorSeq(x):
#     if int(penyebut(x)) % int(x)==0:
#         return str(b)+str(int(penyebut(x)) // int(x))
#     else:
#         return "Tidak ada"

# # Aplikasi
# print(denumeratorSeq('3'))
# print(denumeratorSeq('16'))

def penyebut(x):
    return "9" * len(str(x))

def denumeratorSeq(x):
    if int(penyebut(x)) % int(x) == 0:
        return "Ada: " + str(int(penyebut(x)) // int(x))
    else:
        return "Tidak Ada"
    
print(denumeratorSeq('3'))
print(denumeratorSeq('99'))
print(penyebut('99'))

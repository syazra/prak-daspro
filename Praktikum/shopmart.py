# def harga1(a,b,c):
#     if b=="elektronik" and c==True:
#         return a-(a*30/100)
#     elif b=="elektronik" and c==False:
#         return a-(a*10/100)
#     elif b=="pakaian" and c==True:
#         return a-(a*20/100)
#     elif b=="pakaian" and c==False:
#         return a-(a*5/100)
#     elif b=="makanan" and c==True:
#         return a-(a*15/100)
#     elif b=="makanan" and c==False:
#         return a-(a*2/100)
#     elif b=="lainnya":
#         return a
    
# def harga2(harga1,b,c,e):
#     if e==("Jumat" or "Sabtu") and c==True:
#         return harga1-(harga1*5/100)
#     elif e=="Minggu":
#         return harga1+(harga1*5/100)
#     elif e=="Rabu" and b=="pakaian":
#         return harga1-(harga1*5/100)
#     else:
#         return harga1
    
# def harga3(harga2,d):
#     if d=="dalam negeri":
#         return harga2+(harga2*10/100)
#     else:
#         return harga2+(harga2*20/100)
    
# def hargaAkhir(harga, kategori, VIP, lokasi, hari):
#     return harga3(harga2(harga1(harga,kategori,VIP),kategori,VIP,hari),lokasi)

# print (int(hargaAkhir(500000, "lainnya", True, "dalam negeri", "Kamis")))

def harga1(a,b,c):
    if b=="elektronik" and c==True:
        return a-(a*30/100)
    elif b=="elektronik" and c==False:
        return a-(a*10/100)
    elif b=="pakaian" and c==True:
        return a-(a*20/100)
    elif b=="pakaian" and c==False:
        return a-(a*5/100)
    elif b=="makanan" and c==True:
        return a-(a*15/100)
    elif b=="makanan" and c==False:
        return a-(a*2/100)
    elif b=="lainnya":
        return a
    
def harga2(harga1,b,c,e):
    if e==("Jumat" or "Sabtu") and c==True:
        return harga1-(harga1*5/100)
    elif e=="Minggu":
        return harga1+(harga1*5/100)
    elif e=="Rabu" and b=="pakaian":
        return harga1-(harga1*5/100)
    else:
        return harga1
    
def harga3(harga2,d):
    if d=="dalam negeri":
        return harga2+(harga2*10/100)
    else:
        return harga2+(harga2*20/100)
    
def hargaAkhir(harga, kategori, VIP, lokasi, hari):
    return harga3(harga2(harga1(harga,kategori,VIP),kategori,VIP,hari),lokasi)

print (int(hargaAkhir(500000, "lainnya", True, "dalam negeri", "Kamis")))
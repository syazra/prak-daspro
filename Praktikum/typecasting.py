# x: int
# x=9
# print(str(x))

# a: str
# a='0265745747'
# print(float(a))

# c: bool
# c=False
# print(int(c))

# # def J(j):
# #     if 0 <= j <= 24:
# #         return "Jam:"
# #     else:
# #         return "Waktu tidak valid"
# # def M(m):
# #     if 0 <= m <= 59:
# #         return "Menit:"
# #     else:
# #         return "Waktu tidak valid"
# # def S(s):
# #     if 0<= s <= 59:
# #         return "Detik:"
# #     else:
# #         return "Waktu tidak valid"
# # def jam(j,m,s):
# #     if J(j) and M(m) and S(s):
# #         return j,m,s
# #     else:
# #         return "Waktu tidak valid"
# a="Jam: "
# b=" Menit: "
# c=" Detik: "
# def jam(j,m,s):
#     if 0 <= j <= 24 and 0 <= m <= 59 and 0<= s <= 59:
#         return str(a+str(j)) + "," + str(b+str(m)) + "," + str(c+str(s))
#     else:
#         return "Waktu tidak valid"
# print (jam(1,2,3))

# def jam(j,m,s):
#     if 0 <= j <= 24 and 0 <= m <= 59 and 0<= s <= 59:
#         return ("Jam: ")+ str(j), "Menit:" + str(m), "Detik:" + str(s)
#     else:
#         return "Waktu tidak valid"
# print (jam(1,2,3))

# def monitor_pesawat(x,y,z):
#     if y>900 or y<200:
#         return "Kecepatan Berbahaya"
#     elif x>12000:
#         return "Terlalu Tinggi"
#     elif z<20:
#         return "Bahan Bakar Rendah"
#     elif x<5000 and 200<=y<=900 and z>50:
#         return "Aman untuk Mendarat"
#     else:
#         return "Berjalan Normal"
# print (eval(input()))
# def bawah(x,y):
#     return (x**2+y**2)**0.5
# def jalanSemut(x,y,z):
#     return (bawah(x,z)**2+y**2)**0.5
# print (jalanSemut(1,7,2))
# def s1(x,y,z):
#     return ((x+y)**2+z**2)**0.5
# def s2(x,y,z):
#     return ((y+z)**2+x**2)**0.5
# def s3(x,y,z):
#     return ((z+x)**2+y**2)**0.5
# def js(s1,s2,s3):
#     if s1<s2 and s1<s3:
#         return s1
#     elif s2<s1 and s2<s3:
#         return s2
#     elif s3<s1 and s3<s1:
#         return s3
# def jalanSemut(x,y,z):
#     return js(s1(x,y,z),s2(x,y,z),s3(x,y,z))
# print jalan
# x=jalanSemut
# print (round(x,3))
# def bawah(x,y):
#     return (x**2+y**2)**0.5
# def js1(x,y,z):
#     return ((bawah(x,y))**2+z**2)**0.5
# def js2(x,y,z):
#     return ((bawah(y,z))**2+x**2)**0.5
# def js3(x,y,z):
#     return ((bawah(z,x))**2+y**2)**0.5
# def js(js1,js2,js3):
#     if js1<js2 and js1<js3:
#         return js1
#     elif js2<js1 and js2<js3:
#         return js2
#     elif js3<js1 and js3<js1:
#         return js3
# def jalanSemut(x,y,z):
#     return js((js1(x,y,z)),(js2(x,y,z)),(js3(x,y,z)))
# print (jalanSemut(3,4,5))

# def f(x):
#     return 3*x**2+2*x-5
# def gradien(a,b):
#     return (f(a)-f(b))/(a-b)
# print (gradien(3,1))

# def gradien(a,b):
#     return (3*(a**2)+(2*a)-5)-(3*(b**2)+(2*b)-5)/a-b
# print (gradien(3,1))

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
# def harga2(harga1,d):
#     if d=="dalam negeri":
#         return harga1+(harga1*10/100)
#     else:
#         return harga1+(harga1*20/100)
# def harga3(harga2,b,c,e):
#     if e==("Jumat" or "Sabtu") and c==True:
#         return harga2-(harga2*5/100)
#     elif e=="Minggu":
#         return harga2+(harga2*5/100)
#     elif e=="Rabu" and b=="pakaian":
#         return harga2-(harga2*5/100)
#     else:
#         return harga2
# def hargaAkhir(a,b,c,d,e):
#     return harga3(harga2(harga1(a,b,c),d),b,c,e)
# print (hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin"))

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
#         return harga2
# def harga3(harga2,d):
#     if d=="dalam negeri":
#         return harga2+(harga2*10/100)
#     else:
#         return harga2+(harga2*20/100)
# def hargaAkhir(a,b,c,d,e):
#     return harga3(harga2(harga1(a,b,c),b,c,e),d)
# print (hargaAkhir(1000000, "elektronik", True, "dalam negeri", "Senin"))
# a=" meter"
# def BelajarTenang(x,y):
#     if 15*10**((x-40)/20)<=15000:
#         return "Isi bensin dulu, bang"
#     else:
#         return str(15*10**((x-40)/20)) + str(a)
# x=eval(input())
# print(round(x, 3))

# a=" meter"
# def x1(x):
#     return (15*10**((x-40)/20))

# def x2(x,y,x1):
    
#     if 15*10**((x-40)/20) > y:
#         return "Isi bensin dulu, bang"
#     else:
#         return str(round(x1,3)) + str(a)

# def BelajarTenang(x,y):
#     return x2(x,y,x1(x))
# print(BelajarTenang(102,20000))
print(len('334255'))
a="Ada:"
b="0."
def x(x):
    return 1/len(x)==str(b)+str(x)
print(x('3'))
a="Ada:"
b="0."
def denumeratorSeq(x):
    if 1/len(x)==str(b)+str(x):
        return str(a)+str(x)
    else:
        return "Tidak Ada"
print(denumeratorSeq('3'))

# a=int
# def x(a):
#     return a + 1
# print(x(878727))
# def max2(x,y):
#     return (x+y+abs(x-y))/2
# def min2(x,y):
#     return (x+y-abs(x-y))/2
# print (min2(9,2))
# def ahli(f,g,h):
#     return max2(max2(f,g),h)-min2(min2(f,g),h)
# print (ahli(4000, 5500, 5000))
# def rerata(a):
#     if a=="senin":
#         return (5000+6000+4000)/3
#     elif a=="selasa":
#         return (7000+5000+2000)/3
#     elif a=="rabu":
#         return (4500+3500+3000)/3
#     elif a=="kamis":
#         return (2900+2100+2000)/3
#     elif a=="jumat":
#         return (3000+3000+3000)/3
#     elif a=="sabtu":
#         return (2000+2500+2300)/3
#     elif a=="minggu":
#         return (1100+900+1000)/3
# def pers1(a,b,c,f,g,h):
#     return (c-b)*(ahli(f,g,h))/(rerata(a))
# print(pers1("jumat", 7, 8, 4000, 5500, 5000))
# print(pers1("selasa", 8, 16, 7000, 5000, 2000))
# def pers2(pers1,b,c,d,e,i):
#     if b>e and c<d:
#         return pers1
#     else:
#         pers1*(i/100)
# print (pers2(pers1("selasa", 8, 16, 7000, 5000, 2000), 8, 16, 20, 12,75))
# print (pers2(pers1("jumat", 7, 8, 4000, 5500, 5000),7, 8, 17, 6,3))
# def EstimateGreatLib(a,b,c,d,e,f,g,h,i):
#     return pers2(pers1(a,b,c,f,g,h),b,c,d,e,i)
# print(EstimateGreatLib("selasa", 8, 16, 20, 12, 7000, 5000, 2000, 75))
# print(EstimateGreatLib("jumat", 7, 8, 17, 6, 4000, 5500, 5000, 3))
# import math
# #Keliling Persegi Panjang
# #Def & Spes
# #keliling_persegi_panjang : 2 integer > 0 --> integer
# #keliling_persegi_panjang (x,y) adalah fungsi untuk menghitung keliling persegi panjang dengan panjang x dan lebar y
# #Realisasi
# #keliling_persegi_panjang (x,y) : 2*(x+y)
# #Aplikasi
# #keliling_persegi_panjang (3,5) --> 16
# def keliling_persegi_panjang(x,y):
#     return (2*(x+y))
# print(keliling_persegi_panjang(1,5))

# #Volume Kubus
# def volume_kubus(x: int)-> int:
#     return (x*x*x)
# print(volume_kubus(126))

# #Rata-Rata 4 buah nilai
# def mean(a,b,c,d,w,x,y,z):
#     return (a*w+b*x+c*y+d*z)/(w+x+y+z)
# print(mean(9,13,10,4,2,6,1,5))

# #Nilai Tengah 3 Bilangan
# # med : 3 integer integer
# # med(x,y,z) adalah fungsi untuk mencari nilai tengah dari tiga buah bilangan integer
# # max3 : 3 integer
# #min3
# #min2
# #min2
# def median(a,b,c):
#     return (a+b+c-max3(a,b,c)-min3(a,b,c))
# def max2(a,b):
#     return((a+b)+abs(a-b))//2
# def max3(a,b,c):
#     return max2(max2(a,b),c)
# def min2(a,b):
#     return((a+b)-abs(a-b))//2
# def min3(a,b,c):
#     return min2(min2(a,b),c)
# print(median(1,1,0))

# #Kecepatan Rata-Rata
# #s1 integer >= 0
# #t1 integer > 0
# #s2 integer >= 0
# #t2 integer > 0
# def kecepatan_rata_rata(s1,t1,s2,t2):
#     return (s1/t1)+(s2/t2)/2
# print(kecepatan_rata_rata(17,2,9,2))

# #Jumlah Digit
# def jumlah_digit(x,y,z):
#     return len(x)+len(y)+len(z)
# print(jumlah_digit("1","0","1"))
# # def jumlah_digit(x,y,z):
# #     return len(str(abs(x))+str(abs(y))+str(abs(z)))
# # print(jumlah_digit(-46997979757,8,8598))

# #Volume Bola
# #vol bola 3 integer >0
# #vol bola (r1,r2,r3) adalah fungsi untuk  
# #dif integer >0
# #dif(r1) adalah fungsi untuk menghitung volume bola

# def volume_bola(r1,r2,r3):
#     return (dif(r1)+dif(r2)+dif(r3))
# def dif(x):
#     return (4/3*3.14*x**3)
# print(volume_bola(21,9,15))


# #Jumlah Kombinasi
# def kombinasi(n,r):
#     return ((math.factorial(n))/(math.factorial(r)*math.factorial(n-r)))
# print(kombinasi(100,97))

def mhs(N):
    return [N]
a="kode"
def mhh(s):
    return mhs(str(a) + str(s))

print(mhh(9))
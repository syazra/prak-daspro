# Nama file    : ekspresi_rekursif.py
# Pembuat      : Syafira Azka Ramadhani
# Tanggal      : 1 Oktober 2024
# Deskripsi    : Membuat ekspresi rekursif dari operasi matematika, barisan, dan deret


# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# minus : 2 integer --> integer
# minus(x,y) menghitung hasil pengurangan dari x dan y
# basis    : y = 0 -> x
# rekurens : y < 0 -> minus(x,y+1) + 1
#            y > 0 -> minus(x,y-1) - 1
# REALISASI
def minus(x,y):
    if y == 0:
        return x
    elif y < 0:
        return minus(x,y+1) + 1
    else:
        return minus(x,y-1) - 1
# APLIKASI
print(minus(100,85))
print(minus(0,998))
print(minus(4,-71))
print(minus(-18,2))
print(minus(-12,-12))

# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# mul : 2 integer --> integer
# mul(x,y) menghitung hasil kali dari x dan y
# basis    : x = 0 or y = 0 --> 0
# rekurens : x > 0 and y < 0 --> y + mul(x-1,y)
#            x < 0 and y < 0 --> -x + mul(x,y+1)
#            x > 0 and y > 0 --> x + mul(x,y-1)
# REALISASI
def mul(x,y):
    if y == 0:
        return 0
    elif y > 0:
        return mul(x, y-1) + x
    else:
        return mul(x,y+1) - x
# APLIKASI
print(mul(0,0))
print(mul(9,1))
print(mul(-9,1))
print(mul(9,-1)) 
print(mul(-9,-1))

# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# div : integer >= 0, integer > 0 --> integer
# div(x,y) menghitung hasil bagi dari x dan y dengan hasil sebuah bilangan integer
# basis    : x < y -> 0
# rekurens : x >= y -> 1 + div(x-y,y)
# REALISASI
def div(x,y):
    if x < y:
        return 0
    else:
        return 1 + div(x-y,y)
# APLIKASI
print(div(0,3))
print(div(3,3))
print(div(9,3))

# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# exp : integer, integer >= 0 --> integer
# exp(x,y) menghitung hasil dari memangkatkan sebuah bilangan integer x dengan bilangan integer y
# basis    : y = 0 -> 1
# rekurens : y > 0 -> x * exp(x,y-1)
# REALISASI
def exp(x,y):
    if y == 0:
        return 1
    else:
        return x * exp(x,y-1)
# APLIKASI
print(exp(8,0))
print(exp(-9,3))
print(exp(2,5))

# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# f3 : integer --> integer
# f3(n) menghitung perkalian bilangan integer dengan 3
# basis    : n = 0 -> 0
# rekurens : n < 0 -> -3 + f3(n+1)
#            n > 0 -> 3 + f3(n-1)
# REALISASI
def f3(n):
    if n == 0:
        return 0
    elif n < 0:
        return -3 + f3(n+1)
    else:
        return 3 + f3(n-1) 
# APLIKASI
print(f3(1))
print(f3(21))
print(f3(-21))

# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# s1 : integer > 0 --> integer
# s1(n) menghitung deret bilangan integer: 1 + 2 + 3 + 4 + ...
# basis    : n = 1 -> 1
# rekurens : n > 1 -> n + s1(n-1)
# REALISASI
def s1(n):
    if n == 1:
        return 1
    else:
        return n + s1(n-1)
# APLIKASI
print(s1(1))
print(s1(3))
print(s1(10))

# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# s3 : integer > 0 --> integer
# s3(n) menghitung deret aritmatika: 3 + 6 + 9 + 12 + ...
# basis    : n = 1 -> 3
# rekurens : n > 1 -> 3*n + s3(n-1)
# REALISASI
def s3(n):
    if n == 1:
        return 3
    else:
        return 3*n + s3(n-1)
# APLIKASI
print(s3(1))
print(s3(4))
print(s3(10))

# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# f2 : integer > 0 --> integer
# f2(n) menghitung deret geometri: 1 + 3 + 9 + 27 + ...
# basis    : n = 1 -> 1
# rekurens : n > 1 -> 3**(n-1) + f2(n-1)
# REALISASI
def f2(n):
    if n == 1:
        return 1
    else:
        return 3**(n-1) + f2(n-1)
# APLIKASI
print(f2(1))
print(f2(5))
print(f2(10))

# ==================================================================================================

# DEFINISI DAN SPESIFIKASI
# d1 : integer > 0 --> integer
# d1(n) menghitung deret: 1 + 4 + 9 + 16 + ...
# basis    : n = 1 -> 1
# rekurens : n > 1 -> n**2 + d1(n-1)
# REALISASI
def d1(n):
    if n == 1:
        return 1
    else:
        return n**2 + d1(n-1)
# APLIKASI
print(d1(1))
print(d1(3))
print(d1(8))
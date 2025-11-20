print("Hello, World")

#Pangkat Dua
def fx2(x):
    return x * x
print(fx2(98))

#Pangkat Tiga
def fx3(x):
    return fx2(x) * x
print(fx3(11))

#Perbedaan // dengan /
print(5//2)
print(5/2)

#Maksimum 3
def max2(a, b):
    return (a + b + abs(a - b)) / 2
def max3(a, b, c):
    return max2(max2(a, b), c)
print(max3(100,-20,300))

#Apakah Origin
def is_origin(x,y) :
    return x == 0 and y == 0
print(is_origin(0, 1))
print(is_origin(4.2, 0.0))

#Mean Olympique
def min2(a, b):
    return (a + b - abs(a - b)) / 2
def max4(a, b, c, d):
    return max2(max2(a, b),max2(c, d))
def min4(a, b, c, d):
    return min2(min2(a, b),max2(c, d))
def MO(a, b, c, d):
    return(a + b + c + d - min4(a, b, c, d) - max4(a, b, c, d)) / 2

print(MO(1, 2, 3, 4))
print(MO(-2, 9, 5, 100))

#Apakah Positif
def is_positif(x):
    return x > 0
print(is_positif(0))

#Apakah Huruf A
def is_an_a(x):
    return x == 'a' or x == 'A'
print(is_an_a('p'))

#Apakah Valid
def is_valid(x):
    return x < 5 or x > 190
print(is_valid(5))

#Least Square (Jarak 2 Titik)
def dif2(x, y):
    return fx2(x - y)
def LS(x1, y1, x2, y2):
    return ((dif2(y2, y1) + dif2(x2, x1)) ** (0.5))
print(LS(1,0, -1,0))
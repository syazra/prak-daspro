# Nama: Syafira Azka Ramadhani
# import math

def iskabisat(x):
    return ((x%4==0) and (x%100!=0)) or (x%400==0)
print (iskabisat(2000))

def dpm(m):
    if m==1:
        return 1
    elif m==2:
        return 32
    elif m==3:
        return 60
    elif m==4:
        return 91
    elif m==5:
        return 121
    elif m==6:
        return 152
    elif m==7:
        return 182
    elif m==8:
        return 213
    elif m==9:
        return 244
    elif m==10:
        return 274
    elif m==11:
        return 305
    elif m==12:
        return 335
print (dpm(12))

def jmb(d,m,y):
    return dpm(m)+d-1
print (jmb(31,12,2006))

def jmbk(d,m,y):
    if m>2 and iskabisat(y):
        return dpm(m)+d-1+1
    else:
        return dpm(m)+d-1+0
print (jmbk(1,3,2001))

# no 1
def derajat(x,y):
    if (y=='R'):
        return (4/5*x)
    elif (y=='F'):
        return (9/5*x) +32
    elif (y=='K'):
        return (x+273)
print (derajat(30.0,'R'))   
print (derajat(0,'F')) 
print (derajat(-30.0,'K')) 
# no 2
def temperatur(x):
    if x<=0:
        return "es(padat)"
    elif x>0 and x<100:
        return "cair"
    elif x>=100:
        return "uap"
print (temperatur(180))
print (temperatur(-10))
print (temperatur(0.1))
# no 3
def segitiga(x,y,z):
    if (x==y==z):
        return "segitiga sama sisi"
    elif (x==y!=z) or (x==z!=y) or (y==z!=x):
        return "segitiga sama kaki"
    elif (x!=y!=z):
        return "segitiga sembarang"
print (segitiga(3,3,3))
print (segitiga(5,5,1))
print (segitiga(9,12,3))
# no 4
def D(a,b,c):
    return b**2-4*a*c
def x1(a,b,D):
    return -b+D**0.5/2*a
def x2(a,b,D):
    return -b-D**0.5/2*a
def perbandingan(x1,x2):
    if x1>x2:
        return x1/x2
    else:
        return x2/x1
def hasil_bagi(a,b,c):
    return perbandingan(x1(a,b,D(a,b,c)),x2(a,b,D(a,b,c)))
# print(hasil_bagi(1,0,-4))
# print(hasil_bagi(2,-1,-3))
print(hasil_bagi(1,0,-4))
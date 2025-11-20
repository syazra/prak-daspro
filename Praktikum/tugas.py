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

def jumlah_hari_kabisat(d,m,y):
    if m>2 and iskabisat(y):
        return dpm(m)+d-1+1
    else:
        return dpm(m)+d-1+0
print (jumlah_hari_kabisat(22,3,4))

def isthursday(d,m,y):
    return jumlah_hari_kabisat(d+2,m,y) % 7 == 0
print (isthursday(12,10,2000))
# Konstruktor
def point(x,y):
    return [x,y]

def garis(a,b,c,d):
    return [a,b,c,d]

# Selektor
def absis(p):
    return p[0]

def ordinat(p):
    return p[1]

def garis1(g):
    return g[0]

def garis2(g):
    return g[1]

def garis3(g):
    return g[2]

def garis4(g):
    return g[3]

# Operator
def isBujurSangkar(p1,p2):
    return abs(absis(p1)-absis(p2)) == abs(ordinat(p1)-ordinat(p2))

# def issejajar(p1,p2,p3,p4):
#     return (ordinat(p2)-ordinat(p1))/((absis(p2)-absis(p1))) == (ordinat(p4)-ordinat(p3))/(absis(p4)-absis(p3))
# def diagonal(p1,p2):
#     return ((absis(p1)-absis(p2))**2+(ordinat(p2)-ordinat(p1))**2)**0.5
def gradien(g1,g2,g3,g4):
    return (ordinat(g2)-ordinat(g1)/absis(g2)-absis(g1)) * (ordinat(g4)-ordinat(g3)/absis(g4)-absis(g3)) != -1
def isJajarGenjang(g1,g2,g3,g4):
    if garis1(ordinat(g1))-garis2(ordinat(g2))==garis3(ordinat(g3))-garis4(ordinat(g4)):
        return gradien(g1,g2,g3,g4)
    else:
        return "bantar banh"
    
    # if ordinat(p1) == ordinat(p2) and absis(p1) < absis(p2) and absis(p3) < absis(p4) and issejajar(p1,p2,p3,p4) and issejajar(p1,p3,p2,p4):
    #     return diagonal(p1,p3) == diagonal(p2,p4)
    # elif ordinat(p1) == ordinat(p2) and absis(p1) < absis(p2) and absis(p3) > absis(p4) and issejajar(p1,p2,p3,p4) and issejajar(p1,p4,p2,p4):
    #     return diagonal(p1,p3) == diagonal(p2,p4)
    # elif ordinat(p2) == ordinat(p3) and issejajar(p1,p2,p3,p4) and issejajar(p2,p3,p4,p1):
    #     return diagonal(p1,p2) == diagonal(p3,p4)
    # elif ordinat(p1) == ordinat(p3) and issejajar(p1,p2,p3,p4) and issejajar(p1,p3,p2,p4):
    #     return diagonal(p1,p2) == diagonal(p3,p4)
    
def AreaBujurSangkar(p1,p2):
    if abs(absis(p1)-absis(p2)) == abs(ordinat(p1)-ordinat(p2)):
        return abs(absis(p1)-absis(p2))*abs(ordinat(p1)-ordinat(p2))
    else:
        return "Bukan Bujur Sangkar"

print(isBujurSangkar(point(1,2),point(3,6)))
print(isJajarGenjang(point(1,2),point(4,2),point(6,3),point(3,3)))
print(isJajarGenjang(point(1,2),point(3,3),point(6,3),point(4,2)))
print(AreaBujurSangkar(point(0,0),point(6,6)))
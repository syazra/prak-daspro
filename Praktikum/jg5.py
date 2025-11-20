# Konstruktor
def makePoint(x,y):
    return [x,y]

# Selektor
def absis(p):
    return p[0]

def ordinat(p):
    return p[1]

def panjangAbsis(x1,x2):
    return abs(absis(x1)-absis(x2))

def panjangOrdinat(y1,y2):
    return abs(ordinat(y1)-ordinat(y2))

def gradien(p1,p2):
    if absis(p2)-absis(p1) == 0:
        return (absis(p2)-absis(p1))/(ordinat(p2)-ordinat(p1))
    else:
        return (ordinat(p2)-ordinat(p1))/(absis(p2)-absis(p1))

def isJajarGenjang(p1,p2,p3,p4):
    if ordinat(p1) == ordinat(p2) and ordinat(p3) == ordinat(p4) and ordinat(p1) != ordinat(p3):
        return panjangAbsis(p1,p2) == panjangAbsis(p3,p4) and panjangOrdinat(p1,p3) == panjangOrdinat(p2,p4) and gradien(p1,p3) == gradien(p2,p4) and gradien(p1,p2) * gradien(p2,p4) != -1
    elif ordinat(p2) == ordinat(p3) and ordinat(p1) == ordinat(p4) and ordinat(p2) != ordinat(p1):
        return panjangAbsis(p2,p3) == panjangAbsis(p1,p4) and panjangOrdinat(p2,p1) == panjangOrdinat(p3,p4) and gradien(p2,p1) == gradien(p3,p4) and gradien(p2,p3) * gradien(p3,p4) != -1
    elif ordinat(p1) == ordinat(p3) and ordinat(p2) == ordinat(p4) and ordinat(p1) != ordinat(p2):
        return panjangAbsis(p1,p3) == panjangAbsis(p2,p4) and panjangOrdinat(p1,p2) == panjangOrdinat(p3,p4) and gradien(p1,p2) == gradien(p3,p4) and gradien(p1,p3) * gradien(p3,p4) != -1
    else:
        return False

print(isJajarGenjang(makePoint(1,2),makePoint(4,4),makePoint(4,8),makePoint(1,6)))
print(isJajarGenjang(makePoint(4,2),makePoint(1,2),makePoint(6,4),makePoint(3,4)))
print(isJajarGenjang(makePoint(4,2),makePoint(1,2),makePoint(6,4),makePoint(3,4)))
print(isJajarGenjang(makePoint(1,2),makePoint(3,4),makePoint(4,2),makePoint(6,4)))
print(isJajarGenjang(makePoint(4,0),makePoint(6,4),makePoint(3,4),makePoint(1,0)))
print(isJajarGenjang(makePoint(4,4),makePoint(12,2),makePoint(9,6),makePoint(1,4)))
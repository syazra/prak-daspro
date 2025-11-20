# Konstruktor
def point(x,y):
    return [x,y]

# Selektor
def absis(p):
    return p[0]

def ordinat(p):
    return p[1]

# Operator
def issejajar(p1,p2,p3,p4):
    return (ordinat(p2)-ordinat(p1))/((absis(p2)-absis(p1))) == (ordinat(p4)-ordinat(p3))/(absis(p4)-absis(p3))

print(issejajar(point(1, 2), point(3,4), point(5,6), point(7,8)))

def panjang_garis(p1,p2):
    if ordinat(p1) == ordinat(p2):
        return max(absis(p1),absis(p2))-min(absis(p1),absis(p2))
    elif absis(p1) == absis(p2):
        return max(ordinat(p1),ordinat(p2))-min(ordinat(p1),ordinat(p2))
    else:
        return ((max(absis(p1),absis(p2))-min(absis(p1),absis(p2)))**2+(max(ordinat(p1),ordinat(p2))-min(ordinat(p1),ordinat(p2)))**2)**0.5

print(panjang_garis(point(0,-8), point(0,4)))
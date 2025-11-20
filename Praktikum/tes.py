# Konstruktor
def makePoint(x,y):
    return [x,y]


# Selektor
def absis(p):
    return p[0]

def ordinat(p):
    return p[1]

def diagonal(p1,p2):
    return (absis(p1)+absis(p2))/2 , (ordinat(p1)+ordinat(p2))/2
def isJajarGenjang(p1,p2,p3,p4):
    return (diagonal(p1,p2) == diagonal(p3,p4)) or (diagonal(p1,p3) == diagonal(p2,p4)) or (diagonal(p2,p3) == diagonal(p1,p4))

print(isJajarGenjang(makePoint(1,2),makePoint(4,2),makePoint(6,4),makePoint(3,4)))
print(isJajarGenjang(makePoint(4,2),makePoint(6,4),makePoint(3,4),makePoint(1,2)))
print(isJajarGenjang(makePoint(4,2),makePoint(6,2),makePoint(9,2),makePoint(1,2)))
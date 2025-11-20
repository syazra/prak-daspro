def makePoint(x,y):
    return [x,y]

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

def makeSegiEmpat(P1,P2,P3,P4):
    return [P1,P2,P3,P4]

def titik1(S):
    return S[0]

def titik2(S):
    return S[1]

def titik3(S):
    return S[2]

def titik4(S):
    return S[3]

def gradien(P1,P2):
    return (ordinat(P2)-ordinat(P1))/(absis(P2)-absis(P1))
    
def isJajarGenjang(S):
    if (absis(titik1(S)) == absis(titik2(S)) and absis(titik3(S)) == absis(titik4(S)) and 
            absis(titik1(S)) != absis(titik3(S))):
        return (ordinat(titik1(S)) != ordinat(titik2(S))  and ordinat(titik1(S)) != ordinat(titik3(S)) and ordinat(titik1(S)) != ordinat(titik4(S)) 
                and ordinat(titik2(S)) != ordinat(titik3(S)) and ordinat(titik2(S)) != ordinat(titik4(S)) and ordinat(titik3(S)) != ordinat(titik4(S)))
    elif absis(titik1(S)) == absis(titik3(S)) and absis(titik2(S)) == absis(titik4(S)) and absis(titik1(S)) != absis(titik2(S)):
        return (ordinat(titik1(S)) != ordinat(titik2(S))  and ordinat(titik1(S)) != ordinat(titik3(S)) and ordinat(titik1(S)) != ordinat(titik4(S)) and 
                ordinat(titik2(S)) != ordinat(titik3(S)) and ordinat(titik2(S)) != ordinat(titik4(S)) and ordinat(titik3(S)) != ordinat(titik4(S)))
    elif absis(titik3(S)) == absis(titik2(S)) and absis(titik1(S)) == absis(titik4(S)) and absis(titik3(S)) != absis(titik1(S)):
        return (ordinat(titik1(S)) != ordinat(titik2(S))  and ordinat(titik1(S)) != ordinat(titik3(S)) and ordinat(titik1(S)) != ordinat(titik4(S)) and 
                ordinat(titik2(S)) != ordinat(titik3(S)) and ordinat(titik2(S)) != ordinat(titik4(S)) and ordinat(titik3(S)) != ordinat(titik4(S)))
    elif (absis(titik1(S)) != absis(titik2(S)) and absis(titik3(S)) != absis(titik4(S)) and absis(titik1(S)) != absis(titik3(S)) and absis(titik1(S)) != 
          absis(titik4(S)) and absis(titik2(S)) != absis(titik3(S)) and absis(titik2(S)) != absis(titik4(S))):
        if gradien(titik1(S),titik3(S)) == gradien(titik4(S),titik2(S)) and gradien(titik3(S),titik2(S)) == gradien(titik1(S),titik4(S)):
            return gradien(titik1(S),titik3(S)) * gradien(titik3(S),titik2(S)) != -1
        elif gradien(titik1(S),titik2(S)) == gradien(titik4(S),titik3(S)) and gradien(titik3(S),titik1(S)) == gradien(titik2(S),titik4(S)):
            return gradien(titik1(S),titik2(S)) * gradien(titik3(S),titik1(S)) != -1
        elif gradien(titik1(S),titik2(S)) == gradien(titik4(S),titik3(S)) and gradien(titik4(S),titik1(S)) == gradien(titik2(S),titik3(S)):
            return gradien(titik1(S),titik2(S)) * gradien(titik4(S),titik1(S)) != -1
        else:
            return False
    else:
        return False

print(isJajarGenjang(makeSegiEmpat(makePoint(-6,2),makePoint(-4,2),makePoint(-7,0),makePoint(-3,0))))
print(isJajarGenjang(makeSegiEmpat(makePoint(1,8),makePoint(0,9),makePoint(1,3),makePoint(1,0))))
print(isJajarGenjang(makeSegiEmpat(makePoint(-6,9),makePoint(-1,5),makePoint(-6,-4),makePoint(-1,-4))))
print(isJajarGenjang(makeSegiEmpat(makePoint(-6,2),makePoint(-6,6),makePoint(-6,0),makePoint(-6,4))))
print(isJajarGenjang(makeSegiEmpat(makePoint(-6,6),makePoint(-2,4),makePoint(-6,2),makePoint(-2,0))))
print(isJajarGenjang(makeSegiEmpat(makePoint(-6,2),makePoint(-7,0),makePoint(-2,-6),makePoint(-3,-2))))
print(isJajarGenjang(makeSegiEmpat(makePoint(-2,0),makePoint(-6,2),makePoint(-6,6),makePoint(-2,4))))
print(isJajarGenjang(makeSegiEmpat(makePoint(-6,2),makePoint(-6,6),makePoint(-2,0),makePoint(-2,4))))
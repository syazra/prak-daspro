def makePoint(x,y):
    return [x,y]

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

def makeGaris(P1,P2):
    return [P1,P2]

def titikAwal(G):
    return G[0]

def titikAkhir(G):
    return G[1]

def makeSegiEmpat(G1,G2,G3,G4):
    return [G1,G2,G3,G4]

def garis1(S):
    return S[0]

def garis2(S):
    return S[1]

def garis3(S):
    return S[2]

def garis4(S):
    return S[3]

def gradien(G):
    if (absis(titikAkhir(G))-absis(titikAwal(G))) == 0:
        return 0
    else:
        return (ordinat(titikAkhir(G))-ordinat(titikAwal(G)))/(absis(titikAkhir(G))-absis(titikAwal(G)))
    
def isJajarGenjang(S):
    if gradien(garis1(S)) == gradien(garis2(S)) and gradien(garis3(S)) == gradien(garis4(S)):
        return gradien(garis1(S)) != gradien(garis3(S)) and gradien(garis1(S)) * gradien(garis3(S)) != -1
    elif gradien(garis1(S)) == gradien(garis4(S)) and gradien(garis2(S)) == gradien(garis3(S)):
        return gradien(garis1(S)) != gradien(garis2(S)) and gradien(garis1(S)) * gradien(garis2(S)) != -1
    elif gradien(garis1(S)) == gradien(garis3(S)) and gradien(garis2(S)) == gradien(garis4(S)):
        return gradien(garis1(S)) != gradien(garis2(S)) and gradien(garis1(S)) * gradien(garis2(S)) != -1
    else:
        return False
    
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(1,2),makePoint(1,4)),makeGaris(makePoint(1,4),makePoint(3,4)),makeGaris(makePoint(3,4),makePoint(1,4)),makeGaris(makePoint(1,4),makePoint(1,2)))))
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(1,2),makePoint(4,2)),makeGaris(makePoint(3,4),makePoint(6,4)),makeGaris(makePoint(1,2),makePoint(3,4)),makeGaris(makePoint(4,2),makePoint(6,4)))))
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(-2,7),makePoint(-2,1)),makeGaris(makePoint(-2,1),makePoint(1,2)),makeGaris(makePoint(1,2),makePoint(1,8)),makeGaris(makePoint(1,8),makePoint(-2,7)))))
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(1,2),makePoint(1,8)),makeGaris(makePoint(-2,0),makePoint(-2,8)),makeGaris(makePoint(-2,8),makePoint(1,8)),makeGaris(makePoint(-2,0),makePoint(1,2)))))
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(0,0),makePoint(0,4)),makeGaris(makePoint(0,4),makePoint(4,4)),makeGaris(makePoint(4,4),makePoint(4,0)),makeGaris(makePoint(4,0),makePoint(0,0)))))
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(-6,5),makePoint(-7,1)),makeGaris(makePoint(-7,1),makePoint(-2,1)),makeGaris(makePoint(-2,1),makePoint(-1,5)),makeGaris(makePoint(-1,5),makePoint(-6,5)))))
    
def makePoint(x,y):
    return [x,y]

def X(P):
    return P[0]

def Y(P):
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

def panjangGaris(G):
    return ((X(titikAkhir(G))-X(titikAwal(G)))**2 + (Y(titikAkhir(G))-Y(titikAwal(G)))**2)**0.5

def isSejajar(G1,G2):
    if (X(titikAkhir(G1))-X(titikAwal(G1))) == 0 and (X(titikAkhir(G2))-X(titikAwal(G2))) == 0:
        return True
    elif (X(titikAkhir(G1))-X(titikAwal(G1))) == 0 or (X(titikAkhir(G2))-X(titikAwal(G2))) == 0:
        return False
    else:
        return ((Y(titikAkhir(G1))-Y(titikAwal(G1)))/(X(titikAkhir(G1))-X(titikAwal(G1)))) == ((Y(titikAkhir(G2))-Y(titikAwal(G2)))/(X(titikAkhir(G2))-X(titikAwal(G2))))

def isTegakLurus(G1,G2):
    if (X(titikAkhir(G1))-X(titikAwal(G1))) == 0 or (X(titikAkhir(G2))-X(titikAwal(G2))) == 0:
        return (X(titikAkhir(G1))-X(titikAwal(G1))) != 0 or (X(titikAkhir(G2))-X(titikAwal(G2))) != 0
    else:
        return ((Y(titikAkhir(G1))-Y(titikAwal(G1)))/(X(titikAkhir(G1))-X(titikAwal(G1))) * (Y(titikAkhir(G2))-Y(titikAwal(G2)))/(X(titikAkhir(G2))-X(titikAwal(G2)))) == -1

def isBujurSangkar(S):
    return (panjangGaris(garis1(S)) == panjangGaris(garis2(S)) == panjangGaris(garis3(S)) == panjangGaris(garis4(S))) and isTegakLurus(garis1(S),garis2(S))

def isJajarGenjang(S):
    return panjangGaris(garis1(S)) == panjangGaris(garis3(S)) and panjangGaris(garis2(S)) == panjangGaris(garis4(S)) and isSejajar(garis1(S),garis3(S)) and isSejajar(garis2(S),garis4(S))

print(isBujurSangkar(makeSegiEmpat(makeGaris(makePoint(1,2),makePoint(1,4)),makeGaris(makePoint(1,4),makePoint(3,4)),makeGaris(makePoint(3,4),makePoint(1,4)),makeGaris(makePoint(1,4),makePoint(1,2)))))
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(1,2),makePoint(-2,1)),makeGaris(makePoint(-2,1),makePoint(-2,7)),makeGaris(makePoint(-2,7),makePoint(1,8)),makeGaris(makePoint(1,8),makePoint(1,2)))))
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(-1,7),makePoint(0,1)),makeGaris(makePoint(-2,1),makePoint(1,2)),makeGaris(makePoint(0,2),makePoint(1,8)),makeGaris(makePoint(1,8),makePoint(-2,7)))))
print(isBujurSangkar(makeSegiEmpat(makeGaris(makePoint(1,2),makePoint(4,2)),makeGaris(makePoint(6,4),makePoint(4,2)),makeGaris(makePoint(1,2),makePoint(3,4)),makeGaris(makePoint(3,4),makePoint(6,4)))))
print(isJajarGenjang(makeSegiEmpat(makeGaris(makePoint(-6,5),makePoint(-7,1)),makeGaris(makePoint(-7,1),makePoint(-2,1)),makeGaris(makePoint(-2,1),makePoint(-1,5)),makeGaris(makePoint(-1,5),makePoint(-6,5)))))
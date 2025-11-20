# Syuraih Umar Khotthob_24060124130092
# Praktikum_5_Latihan_Nomor_4

def make_point(x,y):
    return [x,y]

def absis(P):
    return P[0]

def ordinat(P):
    return P[1]

def gradien(G):
    if ordinat(titik_akhir(G)) > ordinat(titik_awal(G)) and absis(titik_akhir(G)) > absis(titik_awal(G)):
        return (ordinat(titik_akhir(G)) - (ordinat(titik_awal(G)))) / ((absis(titik_akhir(G))) - absis(titik_awal(G)))
    else:
        return (ordinat(titik_awal(G)) - (ordinat(titik_akhir(G)))) / ((absis(titik_awal(G))) - absis(titik_akhir(G)))
    
def jarak(g):
    return (((absis(titik_awal(g)) - absis(titik_akhir(g)))**2) + ((ordinat(titik_awal(g)) - ordinat(titik_akhir(g)))**2))**0.5

def make_garis(P1,P2):
    return [P1,P2]

def titik_awal(G):
    return G[0]

def titik_akhir(G):
    return G[1]

def make_segiempat(G1,G2,G3,G4):
    return [G1,G2,G3,G4]

def garis1(G):
    return [G[0],G[1]]

def garis2(G):
    return [G[1],G[2]]

def garis3(G):
    return [G[2],G[3]]

def garis4(G):
    return [G[3],G[4]]

def panjang_garis(G):
    return jarak(G)

def diagonal1(G):
    return ((panjang_garis(garis1(G))**2) + (panjang_garis(garis2(G))**2))**0.5

def diagonal2(G):
    return ((panjang_garis(garis3(G))**2) + (panjang_garis(garis4(G))**2))**0.5

def isBujurSangkar(A):
    #if(absis(titik_awal(garis1())))
    return (panjang_garis(garis1(A)) == panjang_garis(garis2(A)) ) #and (gradien(garis1(A)))*(gradien(garis2(A))) == -1 and gradien(garis1(A)) == gradien(garis3(A))

def isJajargenjang(S):
    return diagonal1(S) > diagonal2(S) or diagonal1(S) < diagonal2(S) and gradien(garis1(S)) == gradien(garis3(S)) and gradien(garis2(S)) == gradien(garis4(S))
print(isBujurSangkar(make_segiempat(make_point(2,2),make_point(2,4),make_point(4,4),make_point(4,2))))
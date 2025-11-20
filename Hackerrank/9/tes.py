# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
def konsLo(L, S):
    return [L] + S

def konsLi(S, L):
    return S + [L]

# DEFINISI DAN SPESIFIKASI SELEKTOR
def FirstList(S):
    return S[0]

def TailList(S):
    return S[1:]

def LastList(S):
    return S[-1]

def HeadList(S):
    return S[:-1]

# DEFINISI DAN SPESIFIKASI PREDIKAT
def IsEmpty(S):
    return S == []

def IsAtom(S):
    return type(S) != list

def IsList(S):
    return type(S) == list

def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        return IsMember(X,TailList(L)) or X == FirstList(L)

def IsMemberLoL(X, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) == X:
                return True
            else:
                return IsMemberLoL(X, TailList(S))
        else:
            return IsMemberLoL(X, FirstList(S)) or IsMemberLoL(X, TailList(S))
        
def ElmtKe(X, S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) == X:
                return 1
            else:
                return 1 + ElmtKe(X, TailList(S))
        else:
            if IsMemberLoL(X, FirstList(S)):
                return 1
            else:
                return 1 + ElmtKe(X, TailList(S))

def Delete(X, S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            return Delete(X, TailList(S))
        else:
            if IsMemberLoL(X, FirstList(S)):
                return FirstList(S)
            else:
                return Delete(X, TailList(S))
    
def findRoute(X, S):
    if IsEmpty(S) or not IsMemberLoL(X, S):
        return []
    else:
        if IsMember(X, S):
            return [ElmtKe(X, S)]
        else:
            return konsLo(ElmtKe(X, S), findRoute(X, Delete(X, S)))


print(findRoute(5, [9, [8, [[91], [99]]], [1, [9, [98]]], [2, [88, [5]]]]))
print(findRoute(0, [1, [2, [[[[[8], 0]]], 4], 5], 6]))

print(findRoute(42, [1,[[],2,[3,[[],[4,[5,[],[[6]]]],7]],[8,[[],9,[10,[[[],11],12]]]],13],[[14,[[],15]],16,[17,[18,[[],[],[19]]]]],[20,[],[21,[22,[23,[],[[[24]]]]]],[[25,[[],26]]]],27,[28,[29,[[],30,[31,[],[[[32]]]]]]],[[33,[],[34,[[],35]]]],36,[37,[[],38,[39,[],[[40,[[],41]]]]]],42,[43,[[],44,[45,[],[[46,[[],47]]]]]],48,[49,[],[50,[[],51,[[[52]]]]]],53,[54,[55,[[],56],[[],57,[58,[[],59]]]]],[[60,[[],[],61]]],62,[63,[[],64,[65,[],[[66]]]]],[[[[67]]]],68,[69,[],[70,[71,[[],72,[[73]]]]]],74,[75,[[],76],[77,[],[[78,[[],79]]]]],80,[81,[82,[83,[],[[84,[[],85]]]]]],[[86,[[],87]]],[[88,[89,[[],90]]]],91,[92,[],93],[[94,[95,[[],[],96]]]],97,[98,[99,[],[[100,[[],101]]]]]])
)
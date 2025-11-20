# Nama File : lol_24060124130088.py
# Pembuat   : Syafira Azka Ramadhani
# Tanggal   : 12 November 2024
# Deskripsi : Membuat type dan operasi list of list


#====================================================================================================================
# TYPE LIST-OF-LIST
#====================================================================================================================

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# KonsLo: list, list of list --> list of list
# KonsLo(L, S) membentuk list baru dengan list (L) yang diberikan sebagai elemen pertama list of list (S)
def KonsLo(L, S):
    return [L] + S

# KonsLi: list of list, list --> list of list
# KonsLi(S, L) membentuk list baru dengan list (L) yang diberikan sebagai elemen terakhir list of list (S)
def KonsLi(S, L):
    return S + [L]

#====================================================================================================================

# DEFINISI DAN SPESIFIKASI SELEKTOR
# FirstList: list of list tidak kosong --> list
# FirstList(S) menghasilkan elemen pertama list of list S, mungkin sebuah list atau atom
def FirstList(S):
    return S[0]

# TailList: list of list tidak kosong --> list of list
# TailList(S) menghasilkan "sisa" list of list S tanpa elemen pertamanya
def TailList(S):
    return S[1:]

# LastList: list of list tidak kosong --> list
# LastList(S) menghasilkan elemen terakhir list of list S, mungkin sebuah list atau atom
def LastList(S):
    return S[-1]

# HeadList: list of list tidak kosong --> list of list
# HeadList(S) menghasilkan "sisa" list of list S tanpa elemen terakhirnya
def HeadList(S):
    return S[:-1]

#====================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT KHUSUS LIST
# IsAtom: list of list --> boolean
# IsAtom(S) benar jika S adalah sebuah atom
def IsAtom(S):
    return type(S) != list

# IsList: list of list --> boolean
# IsList(S) benar jika S adalah sebuah list
def IsList(S):
    return type(S) == list

# IsEmpty: list of list --> boolean
# IsEmpty(S) benar jika S adalah list of list kosong
def IsEmpty(S):
    return S == []

# IsOneElmt: list of list --> boolean
# IsOneElmt(S) benar jika S hanya memiliki satu elemen
def IsOneElmt(S):
    if IsEmpty(S):
        return False
    else:
        return TailList(S) == [] and HeadList(S) == []

#====================================================================================================================

# DEFINISI DAN SPESIFIKASI OPERATOR KHUSUS LIST
# NBElmt: list of list --> integer
# NBElmt(S) menghasilkan banyaknya elemen list, nol jika kosong
def NBElmt(S):
    if IsEmpty(S):
        return 0
    else:
        return 1 + NBElmt(TailList(S))
    
#====================================================================================================================

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsEqS: 2 list of list --> boolean
# IsEqS(S1, S2) benar jika S1 sama dengan S2
def IsEqS(S1, S2):
    if IsEmpty(S1) and IsEmpty(S2):
        return True
    elif IsEmpty(S1) or IsEmpty(S2):
        return False
    else:
        if IsAtom(FirstList(S1)) and IsAtom(FirstList(S2)):
            return FirstList(S1) == FirstList(S2) and IsEqS(TailList(S1), TailList(S2))
        elif IsList(FirstList(S1)) and IsList(FirstList(S2)):
            return IsEqS(FirstList(S1), FirstList(S2)) and IsEqS(TailList(S1), TailList(S2))
        else:
            return False

# IsMemberLS: list, list of list --> boolean
# IsMemberLS(L, S) benar jika list L ada di dalam list of list S
def IsMemberLS(L, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            return IsMemberLS(L, TailList(S))
        else:
            if L == FirstList(S):
                return True
            else:
                return IsMemberLS(L, TailList(S))
        
# IsMemberS: elemen, list of list --> boolean
# IsMemberS(x, S) benar jika elemen x ada di dalam list of list S
def IsMemberS(x, S):
    if IsEmpty(S):
        return False
    else:
        if IsAtom(FirstList(S)):
            if x == FirstList(S):
                return True
            else:
                return IsMemberS(x, TailList(S))
        else:
            return IsMemberS(x, FirstList(S)) or IsMemberS(x, TailList(S))

#====================================================================================================================

# DEFINISI DAN SPESIFIKASI OPERATOR
# Rember: elemen, list of list --> list of list
# Rember(x, S) menghapus semua elemen x yang ada di list of list S
def Rember(x, S):
    if IsEmpty(S):
        return []
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) == x:
                return Rember(x, TailList(S))
            else:
                return KonsLo(FirstList(S), Rember(x, TailList(S)))
        else:
            return KonsLo(Rember(x, FirstList(S)), Rember(x, TailList(S)))
        
# Max: list of list --> elemen
# Max(S) menghasilkan elemen maksimum di dalam list of list S
def Max(S):
    if IsEmpty(S):
        return 0
    # elif IsOneElmt(S):
    #     if IsAtom(FirstList(S)):
    #         return FirstList(S)
    #     else:
    #         return Max(FirstList(S))
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) > Max(TailList(S)):
                return FirstList(S)
            else:
                return Max(TailList(S))
        else:
            if Max(FirstList(S)) > Max(TailList(S)):
                return Max(FirstList(S))
            else:
                return Max(TailList(S))

# NBElmtAtom: list of list --> integer
# NBElmtAtom(S) menghasilkan banyaknya elemen list of list S yang berupa atom
def NBElmtAtom(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            return 1 + NBElmtAtom(TailList(S))
        else:
            return NBElmtAtom(TailList(S))

# NBElmtList: list of list --> integer
# NBElmtList(S) menghasilkan banyaknya elemen list of list yang berupa liast
def NBElmtList(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(FirstList(S)):
            return 1 + NBElmtList(TailList(S))
        else:
            return NBElmtList(TailList(S))
        
# SumLoL: list of list --> integer
# SumLoL(S) menghitung penjumlahan semua elemen dalam list of list S
def SumLoL(S):
    if IsEmpty(S):
        return 0
    else:
        if IsAtom(FirstList(S)):
            return FirstList(S) + SumLoL(TailList(S))
        else:
            return SumLoL(FirstList(S)) + SumLoL(TailList(S))

# MaxNBElmtList: list of list --> integer
# MaxNBElmtList(S) menghasilkan banyaknya elemen list maksimum yang ada pada list of list S
def MaxNBElmtList(S):
    if IsEmpty(S):
        return 0
    else:
        if IsList(FirstList(S)):
            if NBElmt(FirstList(S)) > MaxNBElmtList(TailList(S)):
                return NBElmt(FirstList(S))
            else:
                return MaxNBElmtList(TailList(S))
        else:
            return MaxNBElmtList(TailList(S))

# MaxSumElmt: list of list --> integer
# MaxSumElmt(S) menghasilkan elemen maksimum pada list of list S
#   jika elemen berupa list, maka menghitung penjumlahan dari elemen dalam list tersebut
#   jika elemen berupa atom, maka nilainya adalah elemen tersebut
def MaxSumElmt(S):
    if IsEmpty(S):
        return 0
    elif IsOneElmt(S):
        if IsAtom(FirstList(S)):
            return FirstList(S)
        else:
            return SumLoL(FirstList(S))
    else:
        if IsAtom(FirstList(S)):
            if FirstList(S) > MaxSumElmt(TailList(S)):
                return FirstList(S)
            else:
                return MaxSumElmt(TailList(S))
        else:
            if SumLoL(FirstList(S)) > MaxSumElmt(TailList(S)):
                return SumLoL(FirstList(S))
            else:
                return MaxSumElmt(TailList(S))

#====================================================================================================================

# APLIKASI
# print(KonsLo(2, [3, [1, 2]])) # --> [2, 3, [1, 2]]
# print(KonsLi([2, [0, [8]], 4], [3, 1])) # --> [2, [0, [8]], 4, [3, 1]]
# print(FirstList([[[3], 7, [9]], 0, [8]])) # --> [[3], 7, [9]]
print(TailList([[[3], 7, [9]], [0, [8]]])) # --> [0, [8]]
# print(LastList([[[3], 7, [9]], 0, [8]])) # --> [8]
# print(HeadList([[[3], 7, [9]], 0, [8]])) # --> [[[3], 7, [9]], 0]
# print(IsEmpty([])) # --> True
# print(IsEmpty([[]])) # --> False
# print(IsEqS([1,[[[2],[3, 1]], 4]], [1,[[2,[3, 1]], 4]])) # --> False      
# print(IsEqS([1,[[2,[3, 1]]]], [1,[[2,[3, 1]]]])) # --> True
# print(IsMemberLS([4, 6], [3, [4, 6, 5], [3, 2, 6, 1], 1, 7])) # --> False
# print(IsMemberLS([4, 6, 5], [3, [4, 6, 5], [3, 2, 6, 1], 1, 7])) # --> True
# print(IsMemberS(3, [4, [[8, 9], [0, [2, 3]]], 1])) # --> True
# print(IsMemberS(10, [4, [[8, 9], [0, [2, 3]]], 1])) # --> True
# print(Rember(3, [3, [3, [[3], 3, [3, 3]]]])) # --> [[[[], []]]]
# print(Rember(3, [[[2, 0, [3, 8],4], 7], [3, [[[6, 3]], 9], 5, 3]])) # --> [[[2, 0, [8], 4], 7], [[[[6]], 9], 5]]
print(Max([[[90,[[[[1, [102]]]]], 99,[109], 309]], [100], 90, 190])) # --> 309
print(Max([[[21, [99, [78, 98], 87, [[[[111, 189, [266]]]], 89, [[[[208, 19]]]], 44]]]]])) # --> 266
# print(NBElmtAtom([4, 5, 6, [8, 9, 10], [12, 0], 8])) # --> 4
# print(NBElmtAtom([[2, 0, [8], [9, 1], 7]])) # --> 0
# print(NBElmtList([9, [8, [5], 10]])) # --> 1
# print(NBElmtList([8, [1, [9], 3], [2, [9, 1], 7]])) # --> 2
# print(SumLoL([[[90,[[[[1, [102]]]]], 99,[109], 309]], [100], 90, 190])) # --> 1090
# print(SumLoL([[[21, [99, [78, 98], 87, [[[[111, 189, [266]]]], 89, [[[[208, 19]]]], 44]]]]])) # --> 1309
# print(MaxNBElmtList(([90, [1, [102], 99,[109], 309], [100], 90, 190]))) # --> 5
# print(MaxNBElmtList([21, [99, [78, 98], 87, 111, 189, [266]], 89, [208, 19], 44])) # --> 6
# print(MaxSumElmt([[[90,[[[[1, [102]]]]], 99,[109], 309]], [100], 90, 190])) # --> 710
# print(MaxSumElmt([21, [99, [78, 98], 87, [[[[111, 189, [266]], 89, [[[[208, 19]]]], 44]]]]])) # --> 1288
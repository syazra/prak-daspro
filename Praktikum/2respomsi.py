def IsEmpty(shelves):
    return len(shelves) == 0

def getTag(shelf):
    return shelf[0]

def getBooks(shelf):
    return shelf[1]

def Konso(tag, books):
    return [tag, books]

def Tail(shelves):
    return shelves[1:]

def FirstElmt(shelves):
    return shelves[0]

# FUNGSI KHUSUS
# bersifat opsional, tidak harus digunakan
# boleh buat fungsi antara sendiri

# makeShelf: string, list -> shelf
# fungsi ini membuat sebuah shelf baru dengan komponen tag dan book
def makeShelf(tag, book):
    return [[tag] + [book]]

# AddToShelf: string, list -> shelf
# fungsi ini menambahkan buku ke sebuah shelf dengan tag tertentu
def AddToShelf(books, new_books):
    return books + new_books

# ----------------- FUNCTION ------------------------

def Books(shelves, book):
    if IsEmpty(book):
        return []
    elif IsMemberS(FirstElmt(book), shelves):
        return Books(shelves, Tail(book))
    else:
        return Konso(FirstElmt(book),  Books(shelves, Tail(book)))

# AddBooks: shelves, string, list -> shelves
# fungsi ini mengeluarkan shelves yang sudah ada dengan menambahkan buku ke sebuah shelf dengan tag tertentu
def Ada(shelves, tag, book):
    if IsEmpty(shelves):
        return shelves
    else:
        if getTag(FirstElmt(shelves)) == tag:
            if IsMemberS(FirstElmt(book), shelves):
                return [Konso(tag, AddToShelf(getBooks(FirstElmt(shelves)), Books(shelves, book)))] + Ada(Tail(shelves), tag, book)
            else:
                return [Konso(tag, AddToShelf(getBooks(FirstElmt(shelves)), book))] + Ada(Tail(shelves), tag, book)
        else:
            return [FirstElmt(shelves)] + Ada(Tail(shelves), tag, book)

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

def AddBooks(shelves, tag, book):
    if IsMemberS(tag, shelves):
        return Ada(shelves, tag, book)
    else:
        return shelves + makeShelf(tag, book)
    
# ----------------- APLIKASI ------------------------
print(AddBooks([['Novel', []],
                ['Komputer', ['Clean Code', 'Modern OS', 'Computer Network', 'DSA', 'Algorithms']],
                ['Biologi', ['Sobotta', 'The Selfish Gene', 'Kepunahan Keenam']],
                ['Fisika',['A Brief History of Time', 'The Elegant Universe', 'Astrofisika untuk Orang Sibuk']]],
               "Komputer", ['Clean Code']))
print(AddBooks([['Cerita Anak', ['Matilda', 'Peter Pan']], ['Self Development', ['Atomic Habits', 'The 5 AM Club']]], "Self Development", ['Outliers']))
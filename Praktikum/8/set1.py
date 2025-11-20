# Nama File : set_[nim].py
# Pembuat   : 
# Tanggal   : 
# Deskripsi : Berisi type dan operasi set

from list_operators import *

# DEFINISI DAN SPESIFIKASI TYPE
# Set adalah sebuah list dengan syarat bahwa elemen harus unik
# Semua konstruktor, selektor, dan operasi yang telah didefinisikan
#   untuk list juga berlaku pada set

# DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK SET
# Rember_V1: elemen, list -> list
# Rember_V1(X, L) menghapus sebuah elemen X yang ditemui pertama kali pada list L
#   Jika X ada di dalam list L, maka elemen L berkurang satu
#   Jika X tidak ada di dalam list L maka L tetap
#   List kosong tetap menjadi list kosong
# REALISASI

# Rember_V2: elemen, list -> list
# Rember_V2(X, L) menghapus sebuah elemen X yang ditemui terakhir kali pada list L
#   Jika X ada di dalam list L, maka elemen L berkurang satu
#   Jika X tidak ada di dalam list L maka L tetap
#   List kosong tetap menjadi list kosong
# REALISASI

# MultiRember: elemen, list -> list
# MultiRember(X, L) menghapus semua kemunculan elemen X pada list L
#   List baru yang dihasilkan tidak lagi memiliki elemen X
#   List kosong tetap menjadi list kosong
# REALISASI

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR SET DARI LIST
# MakeSet_V1: list -> set
# MakeSet_V1(L) membuat set dari list L dengan menghapus semua elemen yang muncul lebih dari satu kali
#   dengan memanfaatkan fungsi IsMember(X, L) pada list untuk mengecek duplikasi elemen
#   List kosong tetap menjadi set kosong
# REALISASI

# MakeSet_V2 : list -> set
# MakeSet_V2(L) membuat set dari list L dengan menghapus semua elemen yang muncul lebih dari satu kali
#   dengan memanfaatkan fungsi MultiRember(X, L) pada list untuk menghapus duplikasi elemen
#   List kosong tetap menjadi set kosong
# REALISASI

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR SET
# KonsoSet: elemen, set -> set
# KonsoSet(e, H) menambahkan sebuah elemen e sebagai elemen pertama set H
#   dengan syarat e belum ada di dalam H
# REALISASI

# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: list -> boolean
# IsSet(L) benar jika list L merupakan sebuah set
# REALISASI

# IsSubset: 2 set -> boolean
# IsSubset(H1, H2) benar jika set H1 merupakan subset dari set H2
# REALISASI

# IsEqualSet_V1: 2 set -> boolean
# IsEqualSet_V1(H1, H2) benar jika set H1 adalah set yang sama dengan set H2
#   dengan memanfaatkan fungsi IsSubset(H1, H2)
# REALISASI

# IsEqualSet_V2: 2 set -> boolean
# IsEqualSet_V2(H1, H2) benar jika set H1 adalah set yang sama dengan set H2
#   dengan mengecek satu-persatu elemen pada H1 dan H2
# REALISASI

# IsIntersect: 2 set -> boolean
# IsIntersect(H1, H2) benar jika set H1 beririsan dengan set H2
# REALISASI

# DEFINISI DAN SPESIFIKASI OPERASI TERHADAP SET
# MakeIntersect_V1: 2 set -> set
# MakeIntersect_V1(H1, H2) menghasilkan set baru yang merupakan hasil irisan
#   antara set H1 dan H2 menggunakan rekursif terhadap H1
# REALISASI

# MakeIntersect_V2: 2 set -> set
# MakeIntersect_V2(H1, H2) menghasilkan set baru yang merupakan hasil irisan
#   antara set H1 dan H2 menggunakan rekursif terhadap H2
# REALISASI

# MakeUnion_V1: 2 set -> set
# MakeUnion_V1(H1, H2) menghasilkan set baru yang merupakan hasil gabungan
#   antara set H1 dan H2 menggunakan rekursif terhadap H1
# REALISASI

# MakeUnion_V2: 2 set -> set
# MakeUnion_V2(H1, H2) menghasilkan set baru yang merupakan hasil gabungan
#   antara set H1 dan H2 menggunakan rekursif terhadap H2
# REALISASI

# NBIntersect: 2 set -> integer
# NBIntersect(H1, H2) menghitung jumlah elemen hasil irisan antara set H1 dan H2
#   tanpa memanfaatkan fungsi MakeIntersect(H1, H2)
# REALISASI

# NBUnion: 2 set -> integer
# NBUnion(H1, H2) menghitung jumlah elemen hasil gabungan antara set H1 dan H2
#   tanpa memanfaatkan fungsi MakeUnion(H1, H2)
# REALISASI
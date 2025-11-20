# def max2(x,y):
#     return (x+y+abs(x-y))/2
# def min2(x,y):
#     return (x+y-abs(x-y))/2
# print (min2(9,2))
# def ahli(AS,AM,AIP):
#     return max2(max2(AS,AM),AIP)-min2(min2(AS,AM),AIP)
# print (ahli(4000, 5500, 5000))
# def rerata(D):
#     if D=="senin":
#         return (5000+6000+4000)/3
#     elif D=="selasa":
#         return (7000+5000+2000)/3
#     elif D=="rabu":
#         return (4500+3500+3000)/3
#     elif D=="kamis":
#         return (2900+2100+2000)/3
#     elif D=="jumat":
#         return (3000+3000+3000)/3
#     elif D=="sabtu":
#         return (2000+2500+2300)/3
#     elif D=="minggu":
#         return (1100+900+1000)/3
# def pers1(D,X,Y,SS,SR,AS,AM,AIP,R):
#     if (X>SR and Y<SS):
#         return (Y-X)*(ahli(AS,AM,AIP))/(rerata(D))
#     elif (X<SR and SR<Y):
#         return ((((SR-X)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100)+((Y-SR)*(ahli(AS,AM,AIP))/(rerata(D))))/2
#     elif (SS<Y and X<SS):
#         return ((((Y-SS)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100)+((SS-X)*(ahli(AS,AM,AIP))/(rerata(D))))/2

# def EstimateGreatLib(D,X,Y,SS,SR,AS,AM,AIP,R):
#     return pers1(D,X,Y,SS,SR,AS,AM,AIP,R)
# def max2(x,y):
#     return (x+y+abs(x-y))/2

# def min2(x,y):
#     return (x+y-abs(x-y))/2

# def ahli(AS,AM,AIP):
#     return max2(max2(AS,AM),AIP)-min2(min2(AS,AM),AIP)

# def ahli1(ahli):
#     if ahli==0:
#         return 1
#     else:
#         return ahli

# def rerata(D):
#     if D=="senin":
#         return (5000+6000+4000)/3
#     elif D=="selasa":
#         return (7000+5000+2000)/3
#     elif D=="rabu":
#         return (4500+3500+3000)/3
#     elif D=="kamis":
#         return (2900+2100+2000)/3
#     elif D=="jumat":
#         return (3000+3000+3000)/3
#     elif D=="sabtu":
#         return (2000+2500+2300)/3
#     elif D=="minggu":
#         return (1100+900+1000)/3

# def pers1(D,X,Y,SS,SR,AS,AM,AIP,R):
#     if (X>=SR and Y<=SS):
#         return ((Y-X)*(ahli1(ahli(AS,AM,AIP)))/(rerata(D)))
#     elif (X<SR and Y<SR) or (X==SS and Y>SS) or (Y==SR and X<SR):
#         return ((Y-X)*(ahli1(ahli(AS,AM,AIP)))/(rerata(D)))*R/100
#     elif (X>SS and Y>SS):
#         return ((Y-X)*(ahli1(ahli(AS,AM,AIP)))/(rerata(D)))*R/100
#     elif (X<SR and SR<Y):
#         return ((((SR-X)*(ahli1(ahli(AS,AM,AIP)))/(rerata(D)))*R/100)+((Y-SR)*(ahli(AS,AM,AIP))/(rerata(D))))/2
#     elif (SS<Y and SS>X):
#         return ((((Y-SS)*(ahli1(ahli(AS,AM,AIP)))/(rerata(D)))*R/100)+((SS-X)*(ahli(AS,AM,AIP))/(rerata(D))))/2
#     elif (X<SR and Y>SS):
#         return ((((SR-X)*(ahli1(ahli(AS,AM,AIP)))/(rerata(D)))*R/100)+((SS-SR)*(ahli(AS,AM,AIP))/(rerata(D)))+((((Y-SS)*(ahli(AS,AM,AIP)))/(rerata(D)))*R/100))/3

# def EstimateGreatLib(D,X,Y,SS,SR,AS,AM,AIP,R):
#     return pers1(D,X,Y,SS,SR,AS,AM,AIP,R)

# x=eval(input())
# print(round(x, 5))

# def max2(x,y):
#     return (x+y+abs(x-y))/2

# def min2(x,y):
#     return (x+y-abs(x-y))/2

# def ahli(AS,AM,AIP):
#     return max2(max2(AS,AM),AIP)-min2(min2(AS,AM),AIP)

# def rerata(D):
#     if D=="senin":
#         return (5000+6000+4000)/3
#     elif D=="selasa":
#         return (7000+5000+2000)/3
#     elif D=="rabu":
#         return (4500+3500+3000)/3
#     elif D=="kamis":
#         return (2900+2100+2000)/3
#     elif D=="jumat":
#         return (3000+3000+3000)/3
#     elif D=="sabtu":
#         return (2000+2500+2300)/3
#     elif D=="minggu":
#         return (1100+900+1000)/3

# def pers1(D,X,Y,SS,SR,AS,AM,AIP,R):
#     if (X>=SR and Y<=SS):
#         return ((Y-X)*(ahli(AS,AM,AIP)))/(rerata(D))
#     elif (X<SR and Y<=SR) or (X>=SS and Y>SS):
#         return ((Y-X)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100
#     elif (X<SR and Y<=SS):
#         return ((((SR-X)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100)+((Y-SR)*(ahli(AS,AM,AIP))/(rerata(D))))/2
#     elif (Y>SS and X>=SR):
#         return ((((Y-SS)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100)+((SS-X)*(ahli(AS,AM,AIP))/(rerata(D))))/2
#     elif (X<SR and Y>SS):
#         return ((((SR-X)*(ahli(AS,AM,AIP))/(rerata(D)))*R/100)+((SS-SR)*(ahli(AS,AM,AIP))/(rerata(D)))+((((Y-SS)*(ahli(AS,AM,AIP)))/(rerata(D)))*R/100))/3

# def EstimateGreatLib(D,X,Y,SS,SR,AS,AM,AIP,R):
#     return pers1(D,X,Y,SS,SR,AS,AM,AIP,R)

# x=eval(input())
# print(round(x, 5))

# print(EstimateGreatLib("jumat",1,24,20,4, 8000, 2000, 2000, 75))
# print(round(EstimateGreatLib("jumat", 6, 17, 17, 6, 4000, 5500, 5000, 3),5))
# print(EstimateGreatLib("senin", 12, 17, 18, 9, 6000, 5000, 4500, 50))

# def s1(x,y,z):
#     return round(((x+y)**2+z**2)**0.5,3)
# print(s1(3,4,5))
# def s2(x,y,z):
#     return round(((y+z)**2+x**2)**0.5,3)
# print(s2(3,4,5))
# def s3(x,y,z):
#     return round(((z+x)**2+y**2)**0.5,3)
# print(s3(3,4,5))
# def js(s1,s2,s3):
#     if s1<s2 and s1<s3:
#         return s1
#     elif s2<s1 and s2<s3:
#         return s2
#     elif s3<s1 and s3<s2:
#         return s3
# def jalanSemut(x,y,z):
#     return js(s1(x,y,z),s2(x,y,z),s3(x,y,z))

# print(eval(input()))
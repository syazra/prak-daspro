
# def a(x):
#     return len(str(x))
# print (a('387598748'))
a="0."
b=16
def hasil(x):
    return str(a) + str(x)*b
print(hasil(142857))
def bagisembilan(y):
    return int(y)/9
print(bagisembilan(142857))
def denumeratorSeq(x):
    return len(str(x))*str(bagisembilan(x))
print (denumeratorSeq('142857'))
# c="Ada: "
# def denumeratorSeq(x):
#     if len(str(x))*str(bagisembilan(x))==hasil(x):
#         return str(c)+str(x)
#     else:
#         return "Tidak Ada"
print (denumeratorSeq('142857'))

# def denumeratorSeq(sama):
#     return sama
    
# print(denumeratorSeq(4))
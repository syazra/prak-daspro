# def seq(x):
#     return (int(x)*10**(len(str(x))))/((10**(2*len(str(x))))-(10**len(str(x))))
# print(seq('3'))
a=9
def tes(x):
    return str(a)*len(str(x))
b="Ada: "
def denumeratorSeq(x):
    if int(tes(x)) % int(x)==0:
        return str(b)+str(int(tes(x)) // int(x))
    else:
        return "Tidak ada"
# print(tes1('142857'))
# b="Ada: "
# def denu(x):
#     if int(x)/int(tes(x))==seq(x):
#         return str(b)+str(x)
#     else:
#         return "Tidak ada"
# print(denu('142857'))
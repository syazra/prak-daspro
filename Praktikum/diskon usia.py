def makeDate(d,m,y):
    return [d,m,y]

def day(D):
    return D[0]

def month(D):
    return D[1]

def year(D):
    return D[2]

def MakeDiskon(x,y):
    return [x,y]

def discountCheck(D1,D2):
    if year(D2) - year(D1) <= 2:
        if year(D2) - year(D1) == 2:
            if month(D2) <= month(D1):
                if month(D2) == month(D1):
                    if day(D2) < day(D1):
                        return MakeDiskon("infant", 75)
                    else:
                        return MakeDiskon("child", 25)
                else:
                    return MakeDiskon("infant", 75)
            else:
                return MakeDiskon("child", 25)
        else:
            return MakeDiskon("infant", 75)
    elif (year(D2) - year(D1) > 2) and (year(D2) - year(D1) <= 12):
        if year(D2) - year(D1) == 12:
            if month(D2) <= month(D1):
                if month(D2) == month(D1):
                    if day(D2) < day(D1):
                        return MakeDiskon("child", 25)
                    else:
                        return ["adult", 0]
                else:
                    return MakeDiskon("child", 25)
            else:
                return MakeDiskon("adult", 0)
        else:
            return MakeDiskon("child", 25)
    else:
        return MakeDiskon("adult",0)
   
print(discountCheck(makeDate(1,2,2000), makeDate(1,2,2012)))
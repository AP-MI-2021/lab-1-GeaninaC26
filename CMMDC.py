nr1 = int(input("Dati un numar:"))
nr2 = int(input("Dati un numar:"))
def cmmdc1(nr1, nr2):
    while nr1!=nr2 :
         if nr1>nr2:
            nr1 -= nr2
         else :
            nr2-=nr1
    return nr1


def cmmdc2(nr1,nr2):
    r=nr1%nr2
    while r:
        nr1=nr2
        nr2=r
        r=nr1%nr2
    return nr2


print(cmmdc1(nr1,nr2))

print(cmmdc2(nr1,nr2))




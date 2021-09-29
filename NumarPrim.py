def prim(n):
    if n<=1:
        return False
    for i in range(2, int(n**(1/2))):
        if n % i == 0:
            return False
    return True


n = int(input("citeste numar:"))
print(prim(n))
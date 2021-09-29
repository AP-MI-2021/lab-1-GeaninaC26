from functools import reduce
import operator

'''
Returneaza true daca n este prim si false daca nu.
'''


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** (1 / 2))):
        if n % i == 0:
            return False
    return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    return reduce(operator.mul, lst)


'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc_v1(nr1, nr2):
    r = nr1 % nr2
    while r:
        nr1 = nr2
        nr2 = r
        r = nr1 % nr2
    return nr2


'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''


def get_cmmdc_v2(nr1, nr2):
    while nr1 != nr2:
        if nr1 > nr2:
            nr1 -= nr2
        else:
            nr2 -= nr1
    return nr1


def main():
    n = int(input('n = '))
    print(is_prime(n))
    n = int(input('n = '))
    arr = []
    for i in range(n):
        arr.append(int(input()))
    print(get_product(arr))
    nr1 = int(input('nr1 = '))
    nr2 = int(input('nr2 = '))
    print(get_cmmdc_v1(nr1, nr2))
    print(get_cmmdc_v2(nr1, nr2))


if __name__ == '__main__':
    main()

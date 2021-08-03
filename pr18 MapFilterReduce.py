from functools import reduce


# ***********************************************************************
def square(n):
    return n**2


l1 = [1, 2, 3, 4, 5]
# sq = map(square, l1)
# print(sq)
sq = list(map(square, l1))
print(sq)


# ***********************************************************************
def evenn(n):
    if n % 2 == 0:
        return True
    else:
        return False


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# en = filter(evenn, l1)
# print(en)
en = list(filter(evenn, l1))
print(en)


# ***********************************************************************
def summ(a, b):
    return a + b


l1 = [1, 2, 3, 4]
res = reduce(summ, l1)
print(res)
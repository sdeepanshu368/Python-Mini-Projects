import bisect

l1 = [1, 2, 3, 4, 6, 7, 8, 9, 11, 25, 66, 88]
n = 5
print(bisect.bisect(l1, n))
n = 54
bisect.insort(l1, n)
print(l1)

l2 = ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"]
print(" and ".join(l2))

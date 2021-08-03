lis1 = [30, 36, 29, 42, 57, 71, 33, 12, 2, 74, 78, 62, 64, 71, 65, 89, 96, 86, 100, 77, 98, 81, 11, 11, 43, 1, 29, 11]
print([item for item in lis1 if item % 3 == 0])

dict1 = {'a': 10, 'B': 30, 'A': 50, 'C': 70, 'c': 90}
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

set1 = {x**2 for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
print(set1)

# gen1 = (i for i in range(25))
# for item in gen1:
#     print(item, end=" ")

size = int(input("Enter size of list: "))

mylist = []

for i in range(size):
    mylist.append(int(input("Enter list element: ")))

print(f"Your list is {mylist}\n")

reverse1 = mylist[:]
reverse1.reverse()
print(f"Using First method, reversed list of {mylist} is {reverse1}")

reverse2 = mylist[::-1]
print(f"Using Second method, reversed list of {mylist} is {reverse2}")

reverse3 = mylist[:]
for i in range(len(reverse3) // 2):
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]
    # print(f"the reversed list at i={i} is {reverse3}")
print(f"Using Third method, reversed list of {mylist} is {reverse3}")

if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods are giving the same result\n")

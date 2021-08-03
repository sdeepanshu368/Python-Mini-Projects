import random
n = int(input("Enter the numbers of friends : "))
firstName = []
lastName = []
for i in range(n):
    fname = input(f"Enter the first name of friend {i+1} : ")
    lname = input(f"Enter the last name of friend {i+1} : ")
    firstName.append(fname)
    lastName.append(lname)

random.shuffle(firstName)
random.shuffle(lastName)

print("Here Are Jumbled Names")
for items in zip(firstName,lastName):
    print(" ".join(items))

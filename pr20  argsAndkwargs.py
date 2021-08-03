def func(roll, name, age):
    print("Simple function")
    print(f"The roll no is {roll} and name is {name} and age is {age}")


func(100, "Dev", 21)


# *************************************************************************************************
def func(*args):
    print("\nFunction with *args")
    print(f"The roll no is {args[0]} and name is {args[1]} and age is {args[2]}")


func(100, "Dev", 21)
# one more way is
lis = [100, "Dev", 21]
func(*lis)


# *************************************************************************************************
def func(**kwargs):
    print("\nFunction with **kwargs")
    for key, value in kwargs.items():
        print(f"The name is {key} and age is {value}")


lis2 = {"A": 11, "B": 12, "C": 13, "D": 14, "E": 15, "F": 16, "G": 17, "H": 18}
func(**lis2)


# *************************************************************************************************
def alll(normal, *args, **kwargs):
    print("\nFunction with normal, *args, **kwargs")
    print(normal)
    print(f"The roll no is {args[0]} and name is {args[1]} and age is {args[2]}")
    for key, value in kwargs.items():
        print(f"The name is {key} and age is {value}")


alllis1 = [1, "Peter", 20]
alllis2 = {"A": 21, "B": 22, "C": 23}
alll("John", *alllis1, **alllis2)

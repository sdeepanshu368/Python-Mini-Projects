import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)

    while True:
        try:
            plen = int(input("Enter the password length:\n"))  # length can't be more than 94
            break
        except ValueError:
            print("Oops! That's not a valid number. Please try again...")

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    # Method 1
    # print(s)
    random.shuffle(s)
    # print(s)
    print(f"Your {plen} digit password is:")
    print("".join(s[0:plen]))

    # Method 2
    print(f"Your another {plen} digit password is:")
    print("".join(random.sample(s, plen)))

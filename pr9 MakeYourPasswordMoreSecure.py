'''
Let's secure an existing password by replacing a set of characters with the corresponding 'password-secure' character
Example:
    SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'), ('I', '|'))
    Input:
    Your password = "Indians123"
    Output:
    Your secure password is = "|nd1@n$123"
'''

SECURE = (('s', '$'), ('and', '&'), ('a', '@'), ('o', '0'), ('i', '1'), ('I', '|'))


def securePassword(password):
    for o, n in SECURE:
        password = password.replace(o, n)
    return password


if __name__ == "__main__":
    password = input("Enter your password:\n")
    password = securePassword(password)
    print(f"Your secure password is: {password}")

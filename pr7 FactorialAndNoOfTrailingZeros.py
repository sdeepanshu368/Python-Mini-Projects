def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)


def fTrailingZeroes(number):
    # fac = factorial(number)
    # print(fac)
    count = 0
    i = 5
    while number//i != 0:
        count += int(number/i)
        i = i * 5
    return count


if __name__ == '__main__':
    number = int(input("Enter a number: \n"))
    try:
        fac = factorial(number)
        print(f'The factorial is {fac}')
    except:
        print(f'Oops!!!!!\nFactorial of {number} can not be calculated')

    print('Number of Trailing Zeroes are:', fTrailingZeroes(number))

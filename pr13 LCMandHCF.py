def calclcm():
    a = int(input("Enter first no: "))
    b = int(input("Enter second no: "))
    maxNum = max(a, b)
    temp = maxNum
    while True:
        if maxNum % a == 0 and maxNum % b == 0:
            break
        maxNum = maxNum + temp
    print(f"The LCM of {a} and {b} is {maxNum}")


def calchcf():
    num1 = int(input("Enter first no: "))
    num2 = int(input("Enter second no: "))
    minNum = min(num1, num2)
    for i in range(minNum+1, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
            break
    print(f"The HCF/GCD is {hcf}")


if __name__ == '__main__':
    calclcm()
    calchcf()

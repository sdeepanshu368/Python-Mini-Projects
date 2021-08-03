import random


def wMultiplication(number):
    wrongi = random.randint(1, 8)
    table = [i * number for i in range(1, 11)]
    table[wrongi] = table[wrongi] + random.randint(1, 10)
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i - 1] != i * number:
            return i
    return None


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    myTable = wMultiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at position {wrongIndex}")

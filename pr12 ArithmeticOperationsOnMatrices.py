def matrix(m, n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"Enter o[{i}][{j}]:"))
            row.append(inp)
        o.append(row)
    return o


def sum(a, b):
    output = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        output.append(row)
    return output


def mul():
    A = [[1, 2, 3],
         [4, 5, 6]]
    B = [[10, 11],
         [20, 21],
         [30, 31]]
    C = [[0, 0],
         [0, 0]]
    for i in range(0, len(C)):
        for j in range(0, len(C[0])):
            for k in range(0, len(B)):
                C[i][j] += A[i][k] * B[k][j]
    for row in C:
        print(row)


if __name__ == '__main__':
    m = int(input("Enter the value of row: "))
    n = int(input("Enter the value of column: "))
    print("Enter matrix A:\n")
    A = matrix(m, n)
    print("Enter matrix B:\n")
    B = matrix(m, n)
    s = sum(A, B)
    for row in s:
        print(row)

    mul()

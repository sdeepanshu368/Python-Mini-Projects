import time


# recursive approach
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)


# iterative approach
def iter_fibo(n):
    prevNum = 0
    currNum = 1
    for i in range(1, n):
        prevPrevNum = prevNum
        prevNum = currNum
        currNum = prevPrevNum + prevNum
    return currNum


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    init = time.time()
    print(f"Using iteration value of {num} is {iter_fibo(num)}")
    print(f"Using iteration {time.time() - init} seconds")
    init = time.time()
    print(f"Using recursion value of {num} is {recur_fibo(num)}")
    print(f"Using recursion {time.time() - init} seconds")

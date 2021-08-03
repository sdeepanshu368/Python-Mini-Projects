import time

initial = time.time()
k = 0
while k < 25:
    print("Hello World!")
    # time.sleep(2)
    k += 1
print("While loop ran in", time.time() - initial, "Seconds")

initial2 = time.time()
for i in range(25):
    print("Hello World!")

print("For loop ran in", time.time() - initial2, "Seconds")


seconds = time.time()
print("Seconds since epoch =", seconds)
time.asctime()


time.sleep(5)


localtime = time.asctime(time.localtime(time.time()))
print(localtime)

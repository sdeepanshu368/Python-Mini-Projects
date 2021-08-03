import os


# we can use this function in another file by importing pr21_nameandmainA
def impfunc():
    print("Some important tasks are being done in this function")

# This will also execute automatically upon importing pr21_nameandmainA
# print(os.listdir())
# print("Some important lines of code are written")


def main():
    # This will not execute automatically but we can use this if required
    print(os.listdir())
    print("Some important lines of code are written")


print(__name__)  # will print main in this program but pr21_nameandmainA in file which is importing this file
if __name__ == '__main__':
    # there is no option/way to use this code even if it is required
    # print(os.listdir())
    # print("Some important lines of code are written")
    main()
    impfunc()
    print(__name__)  # will print main in this program and will not execute in another file which is importing this file

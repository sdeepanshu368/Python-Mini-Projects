import os


def myfunc(path, file, formatt):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == formatt:
            os.rename(file, f"{i}{formatt}")
            i += 1


myfunc(r"C:\Users\Intel\PycharmProjects\fp", r"C:\Users\Intel\PycharmProjects\fp\folderfilenamechangerr.py", ".png")

import os


def isword(filename, word):
    with open(filename, 'r') as f:
        filecontent = f.read()
        if word.lower() in filecontent.lower():
            return True
        else:
            return False


if __name__ == '__main__':
    theWord = "Dev"  # enter the word you want to search
    fCount = 0
    dir_contents = os.listdir()
    print(dir_contents)

    for item in dir_contents:
        if item.endswith('txt'):
            print(f"\n*****Searching for {theWord} in {item}*****")
            flag = isword(item, theWord)
            if flag:
                print(f"{theWord} is presented in {item}")
                fCount += 1
            else:
                print(f"{theWord} is not in {item}")

    print(f"\n\n{theWord} detector summery:")
    print(f"{fCount} files contain {theWord}")

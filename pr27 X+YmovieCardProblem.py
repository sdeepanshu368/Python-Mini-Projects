# There are N cards in a row and they can be face up or face down.
# A turn consists of taking two adjacent cards where the left one is face up
# and the right one can be face up or face down and flipping them both.
# Show that this process terminates. (with all the cards facing up).

# Give 0 to face up cards and 1 to face down.
# Initially all the cards are face down so the initial row is 1111...
# A move can either change 10 to 01 or 11 to 00
# and so the resulting number in binary is strictly less than the previous one.
# Thus starting from 1111.. the number decreases with each move, hence the moves must eventually terminate at 000…
# No matter what face down card you choose you will end up getting all face up cards.


def transform(b):
    for i in range(len(b)-1):
        if b[i] == '1':
            b[i] = '0'
            if b[i+1] == '0':
                b[i+1] = '1'
            else:
                b[i+1] = '0'
    return b


if __name__ == "__main__":
    a = list("01111100000111111110111000")
    print(a)
    while a != transform(a.copy()):
        a = transform(a.copy())
    print(a)

"""
Write a function that takes a magic number and a list of numbers. It returns true if it can insert add or subtract operations in the list of numbers to get the magic number. Otherwise, it returns false.

For example:

f(10, [1,2]) = false. There's no way to add or subtract 1 and 2 to get 10.
f(2, [1,2,3,4]) = true. 1 + 2 + 3 - 4 = 2.
f(0, []) = true
f(1, []) = false
f(1, [1]) = true
f(0, [1]) = false

"""


def arithmatic_boggle(magic_number, numbers):
    index = 0
    tmp = 0
    if isMagicNumber(magic_number, numbers, index, tmp):
        print('Magic Number')
        return True
    else:
        print('Not a Magic Number')
        return False

def isMagicNumber(magicNum, arr, ind, tp):
    if len(arr) > ind:
        return (isMagicNumber(magicNum, arr, ind+1, tp+arr[ind]) or isMagicNumber(magicNum, arr, ind+1, tp-arr[ind]))

    if magicNum == tp:
        return True
    else:
        return False

arithmatic_boggle(0, [])

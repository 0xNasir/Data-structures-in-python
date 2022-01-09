from random import random


def buildArrayWithUniqueNumber(arr, size, index):
    rand = int(random() * 100)
    if size > index:
        if rand not in arr:
            arr.append(rand)
            return buildArrayWithUniqueNumber(arr, size, index + 1)
        else:
            return buildArrayWithUniqueNumber(arr, size, index)
    else:
        return arr


if __name__ == '__main__':
    arr = buildArrayWithUniqueNumber([], 100, 0)
    print('Generated List: ', arr)
    key = int(random() * 100)
    print('Generated key: ', key)
    index = -1
    for i in range(len(arr)):
        if arr[i] == key:
            index = i
            break
    if index != -1:
        print('Found at index: ', index)
    else:
        print('Not found')

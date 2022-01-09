from random import random

from Search._linear_search import buildArrayWithUniqueNumber


def binarySearch(arr, key):
    first, last, mid = 0, len(arr) - 1, 0
    output = -1
    while last >= first:
        mid = first + last // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            first = mid+1
        else:
            last = mid-1
    return output


if __name__ == '__main__':
    arr = buildArrayWithUniqueNumber([], 21, 0)
    print('Generated List: ', arr)
    arr.sort()
    print('Sorted list', arr)
    key = int(random() * 100)
    print('Generated key: ', key)
    output = binarySearch(arr, key)

    if output == -1:
        print('Not found')
    else:
        print('Item found at index: ', output)

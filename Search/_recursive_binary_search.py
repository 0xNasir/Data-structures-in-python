from random import random

from Search._linear_search import buildArrayWithUniqueNumber


def recursiveBinarySearch(arr, first, last, key):
    if first <= last:
        mid = (last + first) // 2
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return recursiveBinarySearch(arr, first, mid - 1, key)
        else:
            return recursiveBinarySearch(arr, mid + 1, last, key)
    return -1


if __name__ == '__main__':
    arr = buildArrayWithUniqueNumber([], 21, 0)
    print('Generated List: ', arr)
    arr.sort()
    print('Sorted list', arr)
    key = int(random() * 100)
    print('Generated key: ', key)
    k = recursiveBinarySearch(arr, 0, len(arr) - 1, key)
    if k == -1:
        print('Item is not found in the list')
    else:
        print('Item found at index: ', k)

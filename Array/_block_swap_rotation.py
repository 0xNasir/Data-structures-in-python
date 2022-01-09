def swapElement(arr, first, last, size):
    for i in range(size):
        arr[first + i], arr[last + i] = arr[last + i], arr[first + i]
        print(arr)


def leftRotate(arr, element):
    if element == 0 or element == len(arr):
        return
    i = element
    j = len(arr) - element
    while i != j:
        if i < j:
            swapElement(arr, element - i, element + j - i, i)
            j -= i
        else:
            swapElement(arr, element - i, element, j)
            i -= j
    swapElement(arr, element - i, element, i)


if __name__ == '__main__':
    arr = [i for i in range(1, 8)]
    leftRotate(arr, 3)
    print(arr)

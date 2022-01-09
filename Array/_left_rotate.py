def leftRotateOperation(arr, length):
    temp = arr[0]
    for i in range(length - 1):
        arr[i] = arr[i + 1]
    arr[length - 1] = temp
    print(arr)


def rotareLeft(arr, n, length):
    for i in range(n):
        leftRotateOperation(arr, length)


if __name__ == '__main__':
    n = int(input('Enter an integer number: '))
    arr = [i for i in range(1, n + 1)]
    rotareLeft(arr, n, len(arr))
    print(arr)

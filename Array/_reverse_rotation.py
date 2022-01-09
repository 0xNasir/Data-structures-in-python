def reverseArray(arr, s, e):
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1
        print(arr)


def leftRotate(arr, d, length):
    if d == 0:
        return
    d = d % length
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, length-1)
    reverseArray(arr, 0, length-1)


if __name__ == '__main__':
    arr = [i for i in range(7)]
    print(arr)
    leftRotate(arr, 2, len(arr))
    # print(arr)

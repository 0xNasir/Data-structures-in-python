def cyclicRotation(arr):
    for i in range(len(arr)):
        arr[i], arr[len(arr) - 1] = arr[len(arr) - 1], arr[i]


if __name__ == '__main__':
    arr = [i for i in range(1, 7)]
    cyclicRotation(arr)
    print(arr)

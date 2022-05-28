if __name__ == '__main__':
    str = input('Enter your string here: ')
    start = maxlength = 0
    usedChar = {}
    for i, s in enumerate(str):
        if s in usedChar and start <= usedChar[s]:
            start = usedChar[s] + 1
        else:
            maxlength = max(maxlength, i - start + 1)
        usedChar[s] = i
    print(maxlength)
    print(usedChar)

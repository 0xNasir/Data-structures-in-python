from random import random

if __name__ == '__main__':
    # Declaring list
    list_1 = list()
    list_2 = []
    for i in range(0, 7):
        list_1.append(i)
    print(list_1)
    inline_list = [int(random() * 100) for i in range(0, 7)]
    print(inline_list)
    # Merging two list
    list_2.extend(list_1)
    list_2.extend(inline_list)
    list_2.sort(reverse=False)
    list_2.extend(i for i in range(90, 100))
    print(list_2)
    sum_list = list()
    for i, j in zip(list_1, inline_list):
        sum_list.append(i + j)
    print(sum_list)

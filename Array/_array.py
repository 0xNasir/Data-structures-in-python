import array
if __name__ == '__main__':
    arr=array.array('i', [1,2,3])
    """
    Typecode with python type and memory size
    b----Sign short int----1
    B----Unsign short int----1
    u----unicode character----2
    h----Sign short int----2
    H,i,I----int----2
    l,L----int----4
    q,Q----int----8
    f----float----4
    d----float----8
    """
    print('before append: ', arr.tolist())
    arr.append(4)
    print('after append', arr.tolist())
    arr.insert(4, 5)
    print('after insert',arr.tolist())
    arr.reverse()
    print('after reverse', arr.tolist())
    print('index of 2 is', arr.index(2))
    arr.pop()
    print('after pop', arr.tolist())
    arr.remove(2)
    print('after remove', arr.tolist())
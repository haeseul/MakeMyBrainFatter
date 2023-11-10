def sequentialSearch(a, key):
    n = len(a)
    for i in range(n):
        print(a[i], end=' ')
        if a[i] == key:
            return i
    return -1

def rBinarySearch(a, key, low, high):
    if low > high:          # 못 찾은 경우
        return -1
    else:
        mid = (low + high) // 2
        print(a[mid], end=' ')
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            return rBinarySearch(a, key, low, mid-1)
        else:
            return rBinarySearch(a, key, mid+1, high)

def iBinarySearch(a, key):
    low, high = 0, len(a)-1
    while low <= high:      # 탐색할 원소가 최소 1개는 있다
        mid = (low + high) // 2
        print(a[mid], end=' ')
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == "__main__":
    import random
    from Sorting import selectionSort

    a = []
    for i in range(15):
        a.append(random.randint(1, 100))

    selectionSort(a)
    print('a[] = ', a)

    key = int(input('Input Search Key : ')); print()
    print('Sequential Search : %d' % sequentialSearch(a, key))
    print('rBinary Search : %d' % rBinarySearch(a, key, 0, len(a)))
    print('iBinary Search : %d' % iBinarySearch(a, key))
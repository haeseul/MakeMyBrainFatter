arr = [4, 3, 5, 2, 1]
arr2 = [1,2,3,4,5]
arr3 = [9,6,3,1,2,4,5,7,8]

# Bubble Sort
# 4-line
def bubbleSort(a):
    n = len(a)
    for p in range(1, n):
        print("p = ", p)
        for i in range(1, n - p + 1):
            print("i = ", i)
            print("A[i-1] = ", a[i - 1], ", A[i] = ", a[i])
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
            print("arr = ", arr, "\n")
    return a

# print(bubbleSort(arr))


# Improved Bubble Sort
def bubbleSort2(a):
    n = len(a)
    for p in range(1, n):
        print("p = ", p)
        swapped = False
        for i in range(1, n - p + 1):
            print("i = ", i)
            print("A[i-1] = ", a[i - 1], ", A[i] = ", a[i])
            if a[i - 1] > a[i]:
                a[i - 1], a[i] = a[i], a[i - 1]
                swapped = True
            print("arr = ", a, "\n")
        if swapped is False:
            break
    return a

# print(bubbleSort2(arr))


# Improved Bubble Sort 2
def bubbleSort3(a):
    n = len(a)
    lastSwappedPos = n

    while lastSwappedPos > 0:
        swappedPos = 0
        for i in range(1, lastSwappedPos):
            print("i = ", i)
            print("A[i-1] = ", a[i - 1], ", A[i] = ", a[i])
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                swappedPos = i
        lastSwappedPos = swappedPos
        print("Changed Swapped Pos = ", lastSwappedPos)
        print("arr = ", a, "\n")
    return a

# print(bubbleSort3(arr3))

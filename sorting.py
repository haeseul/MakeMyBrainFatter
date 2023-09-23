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

import math

# Comb Sort
def combSort(a):
    gap = len(a)    # initialize gap size
    shrink = 1.3
    sorted = False  # already sorted or not

    while sorted is False:
        gap = math.floor(gap / shrink)
        print("gap = ", gap)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(a):
            print("i = ", i)
            print("A[i] = ", a[i], ", A[i+gap] = ", a[i+gap])
            if a[i] > a[i+gap]:
                a[i], a[i+gap] = a[i+gap], a[i]
                sorted = False
            i += 1
            print("sorted = ", sorted)
            print("arr = ", a, "\n")
    return a

combSort(arr3)
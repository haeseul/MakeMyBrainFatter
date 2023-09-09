arr = [4, 3, 5, 2, 1]
arr2 = [1,2,3,4,5]
arr3 = [9,6,3,1,2,4,5,7,8]

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

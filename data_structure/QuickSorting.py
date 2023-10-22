import sys
sys.setrecursionlimit(10**7)

def quickSort_Hoare(a, low, high):
    global HoareCmpOps, HoareSwaps
    if high > low:
        pivotPos = partition_Hoare(a, low, high)
        quickSort_Hoare(a, low, pivotPos)     # Lomuto는 pivotPos-1까지
        quickSort_Hoare(a, pivotPos+1, high)
    return HoareSwaps, HoareCmpOps

def partition_Hoare(a, low, high):
    global HoareCmpOps, HoareSwaps
    pivot = a[low]
    i = low-1
    j = high+1

    while True:
        while True:     # pivot 보다 작은 값들 남기기
            i += 1
            HoareCmpOps += 1
            if a[i] >= pivot: break

        while True:     # pivot 보다 큰 값들 남기기
            j -= 1
            HoareCmpOps += 1
            if a[j] <= pivot: break

        if i < j:
            HoareSwaps += 1
            a[i], a[j] = a[j], a[i]
        else:
            return j    # 원소 하나만 남은 경우

def quickSort_Lomuto(a, low, high):
    global LomutoCmpOps, LomutoSwaps
    if high > low:
        pivotPos = partition_Lomuto(a, low, high)
        quickSort_Lomuto(a, low, pivotPos-1)     # Lomuto는 pivotPos-1까지
        quickSort_Lomuto(a, pivotPos+1, high)
    return LomutoCmpOps, LomutoSwaps

def partition_Lomuto(a, low, high):
    global LomutoCmpOps, LomutoSwaps
    pivot = a[low]
    j = low
    for i in range(low+1, high+1):
        LomutoCmpOps += 1
        if a[i] < pivot:
            j += 1
            a[i], a[j] = a[j], a[i]
            LomutoSwaps += 1

    pivotPos = j
    a[low], a[pivotPos] = a[pivotPos], a[low]
    LomutoSwaps += 1
    return pivotPos


if __name__ == '__main__':
    numTestCases = int(input())
    for _ in range(numTestCases):
        HoareSwaps, LomutoSwaps, HoareCmpOps, LomutoCmpOps = 0, 0, 0, 0
        arr = list(map(int, input().split()))
        num = arr.pop(0)

        arr_copy = arr.copy()
        quickSort_Hoare(arr_copy, 0, num - 1)
        arr_copy = arr.copy()
        quickSort_Lomuto(arr_copy, 0, num - 1)
        print(HoareSwaps, LomutoSwaps, HoareCmpOps, LomutoCmpOps)
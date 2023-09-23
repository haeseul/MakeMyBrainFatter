def selectionSort(a, num):
    countCmpOps = 0
    countSwaps = 0

    for i in range(num-1):
        jMin = i

        for j in range(i+1, num):
            countCmpOps += 1
            if a[jMin] > a[j]:
                jMin = j
        if jMin != i:
            countSwaps += 1
            a[jMin], a[i] = a[i], a[jMin]

    print(countCmpOps, countSwaps)

if __name__ == "__main__":
    numTestCases = int(input())

    for i in range(numTestCases):
        a = list(map(int, input().split()))
        num = a.pop(0)
        selectionSort(a, num)
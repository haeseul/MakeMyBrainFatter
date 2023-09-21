def insertionSort(a, num):
    countCmpOps = 0
    countSwaps = 0

    for i in range(1, num):
        for j in range(i, 0, -1):
            countCmpOps += 1
            if a[j-1] > a[j]:
                countSwaps += 1
                a[j-1], a[j] = a[j], a[j-1]
            else:
                break
    print(countCmpOps, countSwaps)

if __name__ == "__main__":
    numTestCases = int(input())

    for i in range(numTestCases):
        a = list(map(int, input().split()))
        num = a.pop(0)
        insertionSort(a, num)
def shellSort(a, num):
    countCmpOps = 0
    countSwaps = 0
    shrinkRatio = 2
    gap = num // shrinkRatio

    while gap > 0:
        for i in range(gap, num):
            for j in range(i, gap-1, -gap):
                countCmpOps += 1
                if a[j-gap] > a[j]:
                    countSwaps += 1
                    a[j-gap], a[j] = a[j], a[j-gap]
                else:
                    break
        gap //= shrinkRatio
    print(countCmpOps, countSwaps)

if __name__ == "__main__":
    numTestCases = int(input())
    for i in range(numTestCases):
        a = list(map(int, input().split()))
        num = a.pop(0)
        shellSort(a, num)
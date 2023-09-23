def bubbleSort(a, n):
    countCmpOps = 0
    countSwaps = 0

    for p in range(1, n):
        for i in range(1, n - p + 1):
            countCmpOps += 1
            if a[i - 1] > a[i]:
                countSwaps += 1
                a[i - 1], a[i] = a[i], a[i - 1]

    return countCmpOps, countSwaps

def bubbleSortImproved1(a, n):
    countCmpOps = 0
    countSwaps = 0

    for p in range(1, n):
        swapped = False
        for i in range(1, n - p + 1):
            countCmpOps += 1
            if a[i - 1] > a[i]:
                countSwaps += 1
                a[i - 1], a[i] = a[i], a[i - 1]
                swapped = True
        if not swapped:
            break

    return countCmpOps, countSwaps

def bubbleSortImproved2(a, n):
    countCmpOps = 0
    countSwaps = 0
    lastSwappedPos = n

    while lastSwappedPos > 0:
        swappedPos = 0
        for i in range(1, lastSwappedPos):
            countCmpOps += 1
            if a[i - 1] > a[i]:
                countSwaps += 1
                a[i - 1], a[i] = a[i], a[i - 1]
                swappedPos = i
        lastSwappedPos = swappedPos

    return countCmpOps, countSwaps

def main():
    numTestCases = int(input())
    results = []

    for i in range(numTestCases):
        b = list(map(int, input().split()))
        num = b.pop(0)

        cmpOps1, swaps1 = bubbleSort(b.copy(), num)
        cmpOps2, swaps2 = bubbleSortImproved1(b.copy(), num)
        cmpOps3, swaps3 = bubbleSortImproved2(b.copy(), num)

        results.append((cmpOps1, swaps1, cmpOps2, swaps2, cmpOps3, swaps3))

    for cmpOps1, swaps1, cmpOps2, swaps2, cmpOps3, swaps3 in results:
        print(f"{cmpOps1} {swaps1} {cmpOps2} {swaps2} {cmpOps3} {swaps3}")

if __name__ == "__main__":
    main()

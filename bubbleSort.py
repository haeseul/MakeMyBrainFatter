def bubbleSort(a, n):
    countCmpOps = 0     # 비교연산자 실행 횟수
    countSwaps = 0      # swap 함수 실행 횟수

    for p in range(1, n):
        for i in range(1, n-p+1):
            countCmpOps += 1
            if a[i-1] > a[i]:
                countSwaps += 1
                a[i-1], a[i] = a[i], a[i-1]

    print(countCmpOps, countSwaps, end=' ')

def bubbleSortImproved1(a, n):
    countCmpOps = 0     # 비교연산자 실행 횟수
    countSwaps = 0      # swap 함수 실행 횟수

    for p in range(1, n):
        swapped = False
        for i in range(1, n-p+1):
            countCmpOps += 1
            if a[i-1] > a[i]:
                countSwaps += 1
                a[i-1], a[i] = a[i], a[i-1]
                swapped = True
        if not swapped:
            break

    print(countCmpOps, countSwaps, end=' ')

def bubbleSortImproved2(a, n):
    countCmpOps = 0     # 비교연산자 실행 횟수
    countSwaps = 0      # swap 함수 실행 횟수
    lastSwappedPos = n

    while lastSwappedPos > 0:
        swappedPos = 0
        for i in range(1, lastSwappedPos):
            countCmpOps += 1
            if a[i-1] > a[i]:
                countSwaps += 1
                a[i-1], a[i] = a[i], a[i-1]
                swappedPos = i
        lastSwappedPos = swappedPos

    print(countCmpOps, countSwaps, end=' ')


if __name__ == "__main__":
    numTestCases = int(input())

    for i in range(numTestCases):
        b = list(map(int, input().split()))
        num = b.pop(0)

        bubbleSort(b.copy(), num)
        bubbleSortImproved1(b.copy(), num)
        bubbleSortImproved2(b.copy(), num)
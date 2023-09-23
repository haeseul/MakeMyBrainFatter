def combSort(a, num):
    countCmpOps = 0  # 비교 연산자 실행 횟수
    countSwaps = 0   # swap 함수 실행 횟수

    # comb sort 알고리즘 구현
    gap = num
    shrink = 1.3
    sorted = False

    while sorted is False:
        gap = max(1, int(gap / shrink))
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < num:
            countCmpOps += 1
            if a[i] > a[i + gap]:
                countSwaps += 1
                a[i], a[i+gap] = a[i+gap], a[i]
                sorted = False
            i += 1
    print(countCmpOps, countSwaps)

if __name__ == "__main__":
    numTestCases = int(input())

    for i in range(numTestCases):
        a = list(map(int, input().split()))
        num = a.pop(0)
        combSort(a, num)
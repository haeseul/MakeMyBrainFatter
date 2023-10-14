def contiSubseq(a, n):
    cnt, maxCnt = 0, 0
    i = 0
    for j in range(1, n):
        if a[i] <= a[j]:
            cnt += 1
        else:
            i = j
            cnt = 0
        if cnt > maxCnt:
            maxCnt = cnt
    return maxCnt + 1


if __name__ == '__main__':
    numTestCases = int(input())
    for _ in range(numTestCases):
        a = list(map(int, input().split()))
        n = a.pop(0)
        print(contiSubseq(a, n))

    # a = [4, 5, 4, 3, 8, 9, 2, 2, 4, 5, 1, 2, 1, 8, 0]
    # b = [1]
    # c = [5, 4, 3, 2, 1]
    # print(contiSubseq(c, len(c)))
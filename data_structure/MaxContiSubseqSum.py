def maxSubsequenceSum(a, n):
    maxSum, thisSum = 0, 0
    start, end = -1, -1
    i = 0
    for j in range(n):
        thisSum += a[j]
        if thisSum > maxSum:
            maxSum = thisSum
            start = i
            end = j
        elif thisSum <= 0:
            i = j + 1
            thisSum = 0
    print(maxSum, start, end)


if __name__ == '__main__':
    numTestCases = int(input())
    for _ in range(numTestCases):
        a = list(map(int, input().split()))
        n = a.pop(0)
        maxSubsequenceSum(a, n)
    # a = [4, -6, 0, 2, 3, -4, 1, 3, 0, -9, 4, 1, -3, 2]
    # b = [-1, 1]
    # c = [-1, -1, -1, -1, 0]
    # d = [5, -7, 2, 3, -4, 5, 2, -7, 8, -7]
    # e = [0, 5, 5, 5]
    # maxSubsequenceSum(e, len(e))

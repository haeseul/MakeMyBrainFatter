def M(i, j):
    if i==j:
        return 0
    if memo[i][j] != -1:
        return memo[i][j]
    memo[i][j] = float('inf')

    for k in range(i, j):
        tmp = M(i, k) + M(k+1, j) + d[i-1]*d[k]*d[j]
        memo[i][j] = min(memo[i][j], tmp)
    return memo[i][j]

numTestCases = int(input())
for _ in range(numTestCases):
    num = int(input())
    d = list(map(int, input().split()))
    memo = [[-1] * (num + 1) for _ in range(num + 1)]
    print(M(1, num))
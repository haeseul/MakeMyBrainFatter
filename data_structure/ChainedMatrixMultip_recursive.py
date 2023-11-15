def M(d, i, j):
    if i==j:
        return 0
    result = float('inf')
    for k in range(i, j):
        tmp = M(d, i, k) + M(d, k+1, j) + d[i-1]*d[k]*d[j]
        result = min(result, tmp)
    return result

numTestCases = int(input())
for _ in range(numTestCases):
    d = list(map(int, input().split()))
    num = d.pop(0)
    print(M(d,1, num))
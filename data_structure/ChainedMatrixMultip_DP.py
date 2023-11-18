def CMM(n, d):
    P = [[0]*(n+1) for _ in range(n+1)]
    M = [[0]*(n+1) for _ in range(n+1)]
    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            M[i][j] = float('inf')
            for k in range(i, j):
                tmp = M[i][k] + M[k+1][j] + d[i-1]*d[k]*d[j]
                if tmp < M[i][j]:
                    M[i][j] = tmp
                    P[i][j] = k
    return M, P

def order(P, i, j):
    if i==j:
        print(f'M{str(i)}', end='')
    else:
        print('(', end='')
        order(P, i, P[i][j])
        order(P, P[i][j]+1, j)
        print(')', end='')

numTestCases = int(input())
for _ in range(numTestCases):
    n = int(input())
    d = list(map(int, input().split()))
    M, P = CMM(n, d)
    order(P, 1, n);print()
    print(M[1][n])
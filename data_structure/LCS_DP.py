def lengthLCS(s, t, m, n):
    global L, S
    for i in range(m+1):
        L[i][0] = 0
    for i in range(n+1):
        L[0][i] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                L[i][j] = L[i-1][j-1]+1
                S[i][j] = 0
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
                if L[i][j] == L[i][j-1]:
                    S[i][j] = 1
                else:
                    S[i][j] = 2
    return L[m][n]

def printLCS(s, t, m, n):
    global S
    if m==0 or n==0:
        return
    if S[m][n] == 0:
        printLCS(s, t, m-1, n-1)
        print(s[m-1], end='')
    elif S[m][n] == 1:
        printLCS(s, t, m, n-1)
    elif S[m][n] == 2:
        printLCS(s, t, m-1, n)

if __name__ == '__main__':
    for _ in range(int(input())):
        a = input().split()
        s = a[0]
        t = a[1]
        m = len(s)
        n = len(t)
        L = [[0]*(n+1) for _ in range(m+1)]
        S = [[0]*(n+1) for _ in range(m+1)]

        print(lengthLCS(s, t, m, n), end=' ')
        printLCS(s, t, m, n)
        print()
        # for i in range(m+1):
        #     for j in range(n+1):
        #         print(L[i][j], end='\t')
        #     print()
        # print()
        # for i in range(m+1):
        #     for j in range(n+1):
        #         print(S[i][j], end='\t')
        #     print()

def lengthLCS(s, t, m, n):
    global memo
    if m<0 or n<0:
        return 0
    if memo[m][n] >= 0:
        return memo[m][n]
    if s[m] == t[n]:
        memo[m][n] = lengthLCS(s, t, m-1, n-1) + 1
        return memo[m][n]
    else:
        memo[m][n] = max(lengthLCS(s, t, m, n-1), lengthLCS(s, t, m-1, n))
        return memo[m][n]

if __name__ == '__main__':
    for _ in range(int(input())):
        a = input().split()
        s = a[0]
        t = a[1]
        m = len(s)
        n = len(t)
        memo = [[-1]*n for _ in range(m)]
        print(lengthLCS(s, t, m-1, n-1))
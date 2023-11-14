def lengthLCS(s, t, m, n):
    global L, S
    if m==0 or n==0:
        return 0
    elif s[m-1] == t[n-1]:
        return lengthLCS(s, t, m-1, n-1) + 1
    else:
        return max(lengthLCS(s, t, m, n-1), lengthLCS(s, t, m-1, n))

if __name__ == '__main__':
    for _ in range(int(input())):
        a = input().split()
        s = a[0]
        t = a[1]
        print(lengthLCS(s, t, len(s), len(t)))
def MAX(a, b):
    return a if a>b else b

def MCSS(a, left, right):
    leftSum, rightSum = 0, 0
    leftMax, rightMax = 0, 0
    if left == right:
        return a[left]

    half = (left + right) // 2

    for i in range(half, left-1, -1):
        leftSum += a[i]
        if leftSum > leftMax:
            leftMax = leftSum

    for i in range(half+1, right+1):
        rightSum += a[i]
        if rightSum > rightMax:
            rightMax = rightSum

    leftTotal = MCSS(a, left, half)
    rightTotal = MCSS(a, half+1, right)
    bigger = MAX(leftTotal, rightTotal)

    mid = MCSS_mid(a, left, half, right)

    biggest = MAX(bigger, mid)
    return biggest



def MCSS_mid(a, left, half, right):
    leftSum, rightSum = 0, 0
    leftMax, rightMax = 0, 0
    for i in range(half, left-1, -1):
        leftSum += a[i]
        if leftSum > leftMax:
            leftMax = leftSum
    for i in range(half+1, right+1):
        rightSum += a[i]
        if rightSum > rightMax:
            rightMax = rightSum
    return leftMax + rightMax

if __name__ == '__main__':
    numTestCases = int(input())
    for _ in range(numTestCases):
        a = list(map(int, input().split()))
        n = a.pop(0)
        print(MCSS(a, 0, n-1))
    # a = [4, -6, 0, 2, 3, -4, 1, 3, 0, -9, 4, 1, -3, 2]
    # b = [-1, 1]
    # c = [-1, -1, -1, -1, 0]
    # d = [5, -7, 2, 3, -4, 5, 2, -7, 8, -7]
    # e = [0, 5, 5, 5]
    # f = [-1, -1, -1, -1, -1]
    # print(MCSS(f, 0, len(f)-1))
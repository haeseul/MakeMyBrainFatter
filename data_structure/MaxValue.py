import sys
sys.setrecursionlimit(10**6)

def Max(a, b):
    if a > b:
        return a
    else:
        return b

def recurMax(a, left, right):
    if left == right:
        return a[left]
    else:
        half = (left + right) // 2
        return Max(recurMax(a, left, half), recurMax(a, half+1, right))


if __name__ == '__main__':
    numTestCases = int(input())
    for _ in range(numTestCases):
        a = list(map(int, input().split()))
        left = 0
        right = a.pop(0) - 1
        print(recurMax(a, left, right))
import sys
sys.setrecursionlimit(10**6)

def binarySearch(a, left, right, value):
    if left > right:
        return -1   # not found (Base case)
    else:
        mid = (left + right) // 2
        if a[mid] == value:
            return mid
        elif a[mid] > value:
            return binarySearch(a, left, mid-1, value)
        else:
            return binarySearch(a, mid+1, right, value)


if __name__ == '__main__':
    numTestCases = int(input())
    for _ in range(numTestCases):
        right, value = map(int, input().split())
        a = list(map(int, input().split()))
        left = 0
        print(binarySearch(a, left, right-1, value))
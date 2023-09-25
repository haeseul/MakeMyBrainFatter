def p(x, n):
    if n == 0:
        return 1
    elif n%2 == 1:
        y = p(x, (n-1)/2)
        return (x*y*y) % 1000
    else:
        y = p(x, n/2)
        return (y*y) % 1000

if __name__ == "__main__":
    numTestCases = int(input())
    for i in range(numTestCases):
        nums = list(map(int, input().split()))
        print(p(nums[0], nums[1]))
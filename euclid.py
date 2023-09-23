def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

if __name__ == "__main__":
    numTestCases = int(input())
    for i in range(numTestCases):
        nums = list(map(int, input().split()))
        print(gcd(nums[0], nums[1]))
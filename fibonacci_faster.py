import sys
sys.setrecursionlimit(10**6)

def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        e = fib(n-1, memo)+fib(n-2, memo)
        memo[n] = e
        return e

if __name__ == "__main__":
    numTestCases = int(input())
    for i in range(numTestCases):
        print(int(str(fib(int(input())))[-3:]))
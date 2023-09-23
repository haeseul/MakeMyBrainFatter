import sys
sys.setrecursionlimit(10**6)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def delete_zero(n):
    reverse = str(n)[::-1]
    result = []
    for a in reverse:
        if a != '0':
            result.append(a)
    print(''.join(result[:3][::-1]))

if __name__ == "__main__":
    numTestCases = int(input())
    for i in range(numTestCases):
        delete_zero(factorial(int(input())))
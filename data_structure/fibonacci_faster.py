def matrix(A, B):
    tmp = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                tmp[i][k] += A[i][j] * B[j][k]
                tmp[i][j] %= 1000
    return tmp

def fib(x, n):
    if n == 0:
        return 0
    elif n == 1:
        return x
    if n%2 == 0:
        tmp = fib(x, n//2)
        return matrix(tmp, tmp)
    else:
        tmp = fib(x, n-1)
        return matrix(x, tmp)

if __name__ == "__main__":
    numTestCases = int(input())
    A = [[1, 1],[1, 0]]
    for _ in range(numTestCases):
        n = int(input())
        if n <= 1:
            print(n)
        else:
            print(fib(A, n)[0][1])